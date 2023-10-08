# pylint: disable=no-member
""" Views for String Rota app """
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .forms import (
    SeatingPositionForm,
    EditSeatingPositionForm,
    PlayerProjectForm,
    ReserveForm,
)
from .models import (
    Project,
    SeatingPlan,
    SeatingPosition,
    Player,
    PlayerProject,
    Section,
)
from .utilities import (
    check_player_project,
    check_seating_plan,
    get_project,
    get_players,
    get_player,
    get_section,
    get_seating_plan,
    get_playing_in_playerproject,
    get_not_playing_in_playerproject,
    get_all_playerproject,
    get_seating_positions,
    get_reserve_vars,
)  # noqa E501


def login(request):
    """Login View"""
    return render(request, "account/login.html")


class Home(View):
    """Home view presents a welcome landing page,
    and populates the sidebar menu with  projects and user
    appropriate options"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)

    def get(self, request):
        """Load projects into sidebar"""
        projects = Project.objects.all()
        sections = Section.objects.all()
        office = request.user.groups.filter(name="Office")
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        section = False
        if not office:
            player = get_player(request)
            section = get_section(player)

        # routine background record checks preventing crashes
        check_player_project()
        check_seating_plan()

        context = {
            "projects": projects,
            "section": section,
            "sections": sections,
            "rota_manager": rota_manager,
            "office": office,
        }
        return render(request, "string_rota/home.html", context)


class Rota(View):
    """Creates rota view for selected project"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Rota, self).dispatch(*args, **kwargs)

    def get(self, request, slug, **kwargs):
        """Creates rota view for selected project"""
        office = request.user.groups.filter(name="Office")
        sections = Section.objects.all()
        project = get_project(slug)
        if office:
            section = get_object_or_404(Section, pk=kwargs["section_id"])
        else:
            try:
                player = get_object_or_404(
                    Player, users_django=request.user.id
                )  # noqa E501
            except player.DoesNotExist:
                messages.warning(request, "You are not logged in as a player.")
                return redirect(reverse("home"))
            section = get_section(player)
        projects = Project.objects.all()

        # no seating_plan record?
        try:
            seating_plan = get_seating_plan(project, section)
        except (
            seating_plan.DoesNotExist
        ):  # no seating plan record for user's section  # noqa E501
            messages.warning(
                request,
                f"There is no Seating \
                Plan for the {section} section for the {project} project.",
            )
            return redirect(reverse("home"))
        all_playerproject = get_all_playerproject(seating_plan, project)
        # no player_in_project record?
        try:
            all_playerproject = get_all_playerproject(
                seating_plan, project
            )  # noqa E501
        except all_playerproject.DoesNotExist():
            messages.warning(
                request,
                f"There are no all_playerproject \
                records for the {project} project. Please contact a manager",
            )
            return redirect(reverse("rota"))

        seating_positions = get_seating_positions(seating_plan)

        res_ply = all_playerproject.filter(performance_status="RE")
        if not res_ply:
            reserve_player = "Not Allocated"
        else:
            reserve_player = res_ply.get()

        playing_in_playerproject = get_playing_in_playerproject(
            seating_plan, project
        )  # noqa E501

        red_ply = playing_in_playerproject.filter(off_reduced_rep=True)
        if not red_ply:
            off_reduced = "Not Allocated"
        else:
            off_reduced = red_ply.all()

        performance_status_na = get_all_playerproject(
            seating_plan, project
        ).filter(  # noqa E501
            performance_status="NA"
        )
        repertoire = project.repertoire_name.all()
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        office = request.user.groups.filter(name="Office")
        strength = section.default_strength
        plan_custom_strength = seating_plan.custom_strength
        if plan_custom_strength:
            strength = plan_custom_strength

        template = "string_rota/rota.html"

        context = {
            "projects": projects,
            "sections": sections,
            "project": project,
            "seating_plan": seating_plan,
            "seating_positions": seating_positions,
            "reserve_player": reserve_player,
            "players_off_reduced_rep": off_reduced,
            "not_available": performance_status_na,
            "repertoire": repertoire,
            "rota_manager": rota_manager,
            "office": office,
            "section": section,
            "strength": strength,
        }
        return render(request, template, context)


class AddSeatingPosition(Rota):
    """Add a player seating position to a Seating Plan"""

    def get(self, request, slug, seating_plan_id):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_plan = get_object_or_404(SeatingPlan, pk=seating_plan_id)

        seating_position_form = SeatingPositionForm(section, seating_plan)
        player_project_form = PlayerProjectForm()

        template = "string_rota/add_sp.html"

        context = {
            "projects": projects,
            "project": project,
            "section": section,
            "seating_position_form": seating_position_form,
            "player_project_form": player_project_form,
        }

        return render(request, template, context)

    def post(self, request, slug, seating_plan_id):
        """Add a Seating Position to a seating plan"""
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_plan = get_object_or_404(SeatingPlan, pk=seating_plan_id)  # noqa E501

        seating_position_form = SeatingPositionForm(
            section, seating_plan, data=request.POST
        )
        player_project = get_object_or_404(
            PlayerProject, player=request.POST.get("player"), project=project
        )

        player_project_form = PlayerProjectForm(
            data=request.POST, instance=player_project
        )

        if seating_position_form.is_valid():
            seating_position_form.instance.seating_plan = seating_plan
            seating_position_form.save()
        else:
            template = "string_rota/add_sp.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "sp_form_errors": seating_position_form.errors,
            }

            return render(request, template, context)

        if player_project_form.is_valid():
            player_project.performance_status = "PL"
            player_project_form.save()
        else:
            template = "string_rota/add_sp.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "pp_form_errors": player_project_form.errors,
            }

            return render(request, template, context)
        messages.success(request, "Your seating position is added ")
        return HttpResponseRedirect(reverse("rota", args=[slug]))


class EditSeatingPosition(Rota):
    """View and Edit the seating positions in a Seating Plan"""

    def get(self, request, slug, seating_position_id):
        projects = Project.objects.all()
        project = get_project(slug)
        player = get_player(request)
        section = get_section(player)
        seating_position = get_object_or_404(
            SeatingPosition, pk=seating_position_id
        )  # noqa E501
        seating_plan = seating_position.seating_plan
        sp_player = seating_position.player
        player_project = get_object_or_404(
            PlayerProject, player=sp_player, project=project
        )

        seating_position_form = EditSeatingPositionForm(
            section, seating_plan, instance=seating_position
        )  # noqa E501
        player_project_form = PlayerProjectForm(instance=player_project)

        template = "string_rota/edit_sp.html"

        context = {
            "player": sp_player,
            "projects": projects,
            "project": project,
            "section": section,
            "position": seating_position,
            "seating_position_form": seating_position_form,
            "player_project_form": player_project_form,
        }

        return render(request, template, context)

    def post(self, request, slug, seating_position_id):
        """Edit a seating position in a seating Plan"""

        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            SeatingPosition, pk=seating_position_id
        )  # noqa E501
        seating_plan = seating_position.seating_plan
        sp_player = seating_position.player
        player_project = get_object_or_404(
            PlayerProject, player=sp_player, project=project
        )

        seating_position_form = EditSeatingPositionForm(
            section, seating_plan, data=request.POST, instance=seating_position
        )
        player_project_form = PlayerProjectForm(
            data=request.POST, instance=player_project
        )

        if seating_position_form.is_valid():
            seating_position_form.save()
        else:
            template = "string_rota/edit_sp.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "position": seating_position,
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "seating_position_form_errors": seating_position_form.errors,
                "player_project_form_errors": player_project_form.errors,
            }

            return render(request, template, context)

        if player_project_form.is_valid():
            player_project_form.save()
        else:
            print("player_project_form is not valid")
            template = "string_rota/edit_sp.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "pp_form_errors": player_project_form.errors,
            }

            return render(request, template, context)
        messages.success(request, "Your seating position is updated ")

        return HttpResponseRedirect(reverse("rota", args=[slug]))


class Reserve(Rota):
    """Set the Reserve and Reduced status for a plyer iin a project"""

    def get(self, request, slug):
        projects = Project.objects.all()

        (
            project,
            section,
            seating_plan,
            not_playing_in_playerproject,
        ) = get_reserve_vars(request, slug)

        reserve_form = ReserveForm(section, seating_plan)

        template = "string_rota/reserve.html"

        context = {
            "projects": projects,
            "project": project,
            "section": section,
            "reserve_form": reserve_form,
            "not_playing_in_playerproject": not_playing_in_playerproject,
        }

        return render(request, template, context)

    def post(self, request, slug):
        """Saves reserve status for player in project"""

        projects = Project.objects.all()
        project = get_project(slug)
        player = get_player(request)
        section = get_section(player)
        players = get_players(section)
        seating_plan = get_seating_plan(project, section)
        not_playing_in_playerproject = get_not_playing_in_playerproject(
            players, seating_plan, project
        )  # noqa E501

        reserve_form = ReserveForm(
            section,
            seating_plan,
            data=request.POST,
        )
        if reserve_form.is_valid():
            print("reserve form valid")
            plpr_from_form = get_object_or_404(
                PlayerProject,
                project=project,
                player=reserve_form.instance.player,  # noqa E501
            )

            # set all execept form_player status to "NA"
            for player_plpr in not_playing_in_playerproject:
                plpr = get_object_or_404(
                    PlayerProject,
                    project=project,
                    player=player_plpr.player,  # noqa E501
                )
                if plpr != plpr_from_form:
                    if plpr.performance_status == "RE":
                        plpr.performance_status = "NA"
                        plpr.save()
                        messages.success(
                            request,
                            f"{plpr.player} is no longer Reserve",  # noqa E501
                        )
            # toggle performance status of selected player
            if plpr_from_form.performance_status == "RE":
                # remove Reserve status
                plpr_from_form.performance_status = "NA"
                messages.success(
                    request,
                    f"{plpr_from_form.player} is no longer the Reserve player",  # noqa E501
                )
            else:
                # set status to Reserve
                plpr_from_form.performance_status = "RE"
                messages.success(
                    request,
                    f"{plpr_from_form.player} is now  the Reserve player",  # noqa E501
                )
            plpr_from_form.save()

        else:
            print("reserve form not valid")
            template = "string_rota/reserve.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "reserve_form": reserve_form,
                "reserve_form.errors": reserve_form.errors,
                "not_playing_in_playerproject": not_playing_in_playerproject,
            }

            return render(request, template, context)

        return HttpResponseRedirect(reverse("rota", args=[slug]))


class DeleteSeatingPosition(View):
    """Delete a seating position in a project"""

    def get(self, request, slug, position_id):
        """Logic for deleting a seating position"""
        seating_position = get_object_or_404(
            SeatingPosition, id=position_id
        )  # noqa E501
        player = seating_position.player
        project = seating_position.seating_plan.project
        player_project = get_object_or_404(
            PlayerProject, project=project, player=player
        )  # noqa E501

        seating_position.delete()

        player_project.performance_status = "NA"
        player_project.off_reduced_rep = False
        player_project.save(
            update_fields=["performance_status", "off_reduced_rep"]
        )  # noqa E501

        messages.success(
            request, f"{player.first_name} has been removed from this rota."
        )  # noqa E501
        return HttpResponseRedirect(reverse("rota", args=[slug]))


class ToggleSeatingPlanStatus(Rota):
    """Toggle the status of a seating plan from draft to published"""

    def get(self, request, slug, seating_plan_id):
        print("ToggleSeatingPlanStatus called")

        project = get_project(slug)
        player = get_player(request)
        section = get_section(player)
        seating_plan = get_seating_plan(project, section)

        status = seating_plan.plan_status

        if status == "D":
            seating_plan.plan_status = "P"
            seating_plan.save()
            messages.success(
                request,
                f"The {section} section Rota for {project} is now Published",  # noqa E501
            )  # noqa E501
        else:
            seating_plan.plan_status = "D"
            seating_plan.save()
            messages.success(
                request,
                f"The {section} section Rota for {project} is set to  Draft and is not viewable by players or office",  # noqa E501
            )  # noqa E501

        return HttpResponseRedirect(reverse("rota", args=[slug]))
