# pylint: disable=no-member
""" Views for String Rota app """
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.contrib.auth.models import User, Group
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
    # Section,
    PlayerProject,
)
from .utilities import (
    check_player_project,
    check_seating_plan,
    get_project,
    get_players,
    get_player,
    get_section,
    get_seating_plan,
    # get_available_in_playerproject,
    get_playing_in_playerproject,
    get_all_playerproject,
    get_seating_positions,
    get_reserve_vars,
)  # noqa E501


def login(request):
    """Login View"""
    return render(request, "account/login.html")


class Projects(View):
    """Home view loading projects in the sidebar"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Projects, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Loads projects into sidebar"""
        projects = Project.objects.all()

        # routine background record checks preventing crashes
        check_player_project()
        check_seating_plan()

        context = {
            "projects": projects,
        }
        return render(request, "string_rota/home.html", context)


class Rota(Projects):
    """Creates rota view for selected project"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Rota, self).dispatch(*args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        """Creates rota view for selected project"""

        try:
            player = get_object_or_404(Player, users_django=request.user.id)
        except player.DoesNotExist:
            messages.warning(request, "You are not logged in as a player.")
            return redirect(reverse("projects"))
        projects = Project.objects.all()
        project = get_project(slug)
        section = get_section(player)
        players = get_players(section)

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
            return redirect(reverse("projects"))
        all_playerproject = get_all_playerproject(seating_plan, project)
        # no player_in_project record?
        try:
            all_playerproject = get_all_playerproject(
                seating_plan, project
            )  # noqa E501
        except Exception:
            messages.warning(
                request,
                f"There are no all_playerproject \
                records for the {project} project.",
            )
            return redirect(reverse("projects"))

        seating_positions = get_seating_positions(seating_plan)

        res_ply = all_playerproject.filter(performance_status="RE")
        print(f"all_playerproject: {all_playerproject}")
        print(f"reserved players in all_playerproject {res_ply}")
        if not res_ply:
            reserve_player = "Not Allocated"
        else:
            reserve_player = res_ply.get()

        playing_in_playerproject = get_playing_in_playerproject(
            players, seating_plan, project
        )

        red_ply = playing_in_playerproject.filter(off_reduced_rep=True)
        print(f"playing_in_playerproject: {playing_in_playerproject}")
        print(f"reduced players in playing_in_playerproject: {red_ply}")
        if not red_ply:
            off_reduced = "Not Allocated"
        else:
            off_reduced = red_ply.all()

        not_available = get_all_playerproject(seating_plan, project).filter(
            performance_status="NA"
        )
        repertoire = project.repertoire_name.all()
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        strength = section.default_strength
        plan_custom_strength = seating_plan.custom_strength
        if plan_custom_strength:
            strength = plan_custom_strength

        template = "string_rota/home.html"

        context = {
            "playing_in_playerproject": playing_in_playerproject,
            "projects": projects,
            "project": project,
            "seating_plan": seating_plan,
            "seating_positions": seating_positions,
            # "players": players_in_project,
            "reserve_player": reserve_player,
            "players_off_reduced_rep": off_reduced,
            "not_available": not_available,
            "repertoire": repertoire,
            "rota_manager": rota_manager,
            "section": section,
            "strength": strength,
        }
        return render(request, template, context)


class AddSeatingPosition(Rota):
    """Add a player seating position to a Seating Plan"""

    def get(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_plan = get_object_or_404(
            SeatingPlan, project=project, section=section
        )  # noqa E501

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

    def post(self, request, slug, seating_plan_id, *args, **kwargs):
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

    def get(self, request, slug, seating_position_id, *args, **kwargs):
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

    def post(self, request, slug, seating_position_id, *args, **kwargs):
        """Edit a seating position in a seating Plan"""

        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            SeatingPosition, id=seating_position_id
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
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "seating_position_form_errors": seating_position_form.errors,
                "player_project_form_errors": player_project_form.errors,
            }

            return render(request, template, context)

        if player_project_form.is_valid():
            player_project_form.save()
        else:
            print(f"player_project_form is not valid")
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

    def get(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()

        (
            playing_in_playerproject,
            section,
            seating_plan,
            project,
            available_players,
        ) = get_reserve_vars(request, slug)
        print(f"project slug: {project.slug}")

        reserve_form = ReserveForm(section, seating_plan)

        template = "string_rota/reserve.html"

        context = {
            "playing_in_playerproject": playing_in_playerproject,
            "projects": projects,
            "project": project,
            "section": section,
            "available_players": available_players,
            "reserve_form": reserve_form,
        }

        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        """Saves reserve status for player in project"""
        projects = Project.objects.all()
        project = get_project(slug)
        player = get_player(request)
        section = get_section(player)
        players = get_players(section)
        seating_plan = get_seating_plan(project, section)
        playing_in_playerproject = get_playing_in_playerproject(
            players, seating_plan, project
        )  # noqa E501

        reserve_form = ReserveForm(
            section,
            seating_plan,
            data=request.POST,
            # instance=players_in_project,  # noqa E501
        )

        if reserve_form.is_valid():
            reserve_form.save()
        else:
            template = "string_rota/reserve.html"

            context = {
                "players_in_project": playing_in_playerproject,
                "projects": projects,
                "project": project,
                "section": section,
                "available_players": available_players,
                "reserve_form": reserve_form,
                "reserve_form.errors": reserve_form.errors,
            }

            return render(request, template, context)

        messages.success(request, "Your Reserve Player has been allocated")
        return HttpResponseRedirect(reverse("rota", args=[slug]))


class DeleteSeatingPosition(View):
    """Delete a seating position in a project"""

    def get(self, request, slug, position_id, *args, **kwargs):
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


class ChangePlanStatus(View):
    """Change the status of a seating plan"""

    def get():
        pass
