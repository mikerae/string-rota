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
    ReserveReducedForm,
)
from .models import (
    Project,
    SeatingPlan,
    SeatingPosition,
    Player,
    Section,
    PlayerProject,
)
from .utilities import check_player_project, check_seating_plan


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
        print("rota is called")
        projects = Project.objects.all()
        project = get_object_or_404(Project, slug=slug)

        sections = Section.objects.all()
        # check if user is not a player, & is a manager
        try:
            player = get_object_or_404(Player, users_django=request.user.id)
        except player.DoesNotExist as error:
            print(f"You are not logged in as a player. {error}")
            messages.warning(request, "You are not logged in as a player.")
            return redirect(reverse("projects"))

        section = player.section
        # no player_in_project record?
        try:
            players_in_project = PlayerProject.objects.filter(
                project=project
            ).filter(  # noqa E501
                player__section=section
            )
        except Exception as e:
            print(
                f"There is no player_in_project for the {project} project. \
                players_in_project: {players_in_project} {e}"
            )
            messages.warning(
                request,
                f"There is no players_in_project \
                record for the {project} project.",
            )
            return redirect(reverse("projects"))

        queryset = SeatingPlan.objects.filter(
            project=project,
        )
        if not queryset:  # no seating plan records for this project
            print(f"queryset: {queryset} for seating plan, project: {project}")
            print(f"There are no Seating Plans for the {project} project.")
            messages.warning(
                request,
                f"There are no Seating \
                Plans for the {project} project.",
            )
            return redirect(reverse("projects"))

        try:
            seating_plan = get_object_or_404(queryset, section=section.id)
        except Exception:  # no seating plan record for user's section
            print(
                f"There is no Seating Plan for the {section} section for \
                the {project} project."
            )
            messages.warning(
                request,
                f"There is no Seating \
                Plan for the {section} section for the {project} project.",
            )
            return redirect(reverse("projects"))
        print(f"seating plan: {seating_plan}")

        seating_positions = SeatingPosition.objects.filter(
            seating_plan=seating_plan
        ).order_by("position_number")

        res_ply = players_in_project.filter(performance_status="RE")
        if not res_ply:
            reserve_player = "Not Allocated"
        else:
            reserve_player = res_ply.get()

        red_ply = players_in_project.filter(off_reduced_rep=True)
        if not red_ply:
            off_reduced = "Not Allocated"
        else:
            off_reduced = red_ply.all()
        not_available = players_in_project.filter(performance_status="NA")
        repertoire = project.repertoire_name.all()
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        print(f"reserve_player: {reserve_player}")
        print(f"player_off_reduced_rep: {off_reduced}")
        strength = section.default_strength
        plan_custom_strength = seating_plan.custom_strength
        if plan_custom_strength:
            strength = plan_custom_strength
        print(f"This Project needs {strength} players in the {section} section")

        context = {
            "projects": projects,
            "project": project,
            "seating_plan": seating_plan,
            "seating_positions": seating_positions,
            "players": players_in_project,
            "reserve_player": reserve_player,
            "players_off_reduced_rep": off_reduced,
            "not_available": not_available,
            "repertoire": repertoire,
            "rota_manager": rota_manager,
            "section": section,
            "strength": strength,
        }
        return render(request, "string_rota/home.html", context)


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
        print(f"seating position : {seating_position}")
        print(f"player : {sp_player}")

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
            print("edited seating plan is valid")
        else:
            print("edited seating plan is not valid")
            template = "string_rota/edit_sp.html"

            context = {
                "projects": projects,
                "project": project,
                "section": section,
                "seating_position_form": seating_position_form,
                "player_project_form": player_project_form,
                "sp_form_errors": seating_position_form.errors,
                "pp_form_errors": player_project_form.errors,
            }

            return render(request, template, context)

        if player_project_form.is_valid():
            player_project_form.save()
        else:
            print("edited player_project_form not valid")
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


class EditPlayerProject(Rota):
    """View and edit the player details for a given project"""

    def get(self, request, slug, player_pp_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        player_pp = get_object_or_404(Player, id=player_pp_id)
        player_project = get_object_or_404(
            PlayerProject, player=player_pp, project=project
        )

        player_project_form = EditPlayerProjectForm(instance=player_project)

        context = {
            "projects": projects,
            "project": project,
            "player": sp_player,
            "section": section,
            "player_project_form": player_project_form,
        }

        return render(request, "string_rota/edit_pp.html", context)

    def post(self, request, slug, player_pp_id, *args, **kwargs):
        """Edit the player details for a given project"""
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        player_pp = get_object_or_404(Player, id=player_pp_id)
        player_project = get_object_or_404(
            PlayerProject, player=player_pp, project=project
        )

        player_project_form = EditPlayerProjectForm(
            data=request.POST, instance=player_project
        )

        if player_project_form.is_valid():
            player_project_form.save()

        return HttpResponseRedirect(reverse("rota", args=[slug]))


class ReserveReduced(Rota):
    """Set the Reserve and Reduced status for a plyer iin a project"""

    def get(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        players_project = PlayerProject.objects.filter(project=project).filter(
            player__section=section
        )
        print(f"players_project: {players_project}")
        reserve_reduced_form = ReserveReducedForm()

        context = {
            "projects": projects,
            "project": project,
            "section": section,
            "players_project": players_project,
            "reserve_reduced_form": reserve_reduced_form,
        }

        return render(request, "string_rota/reserve_reduced.html", context)

    # def post(self, request, *args, **kwargs):
    #     projects = Project.objects.all()
    #     project = get_object_or_404(projects, slug=slug)
    #     player = get_object_or_404(Player, users_django=request.user.id)
    #     section = player.section
    #     player_pp = get_object_or_404(Player, id=player_pp_id)
    #     player_project = get_object_or_404(
    #         PlayerProject,
    #         player=player_pp,
    #         project=project
    #         )

    #     reserve_reduced_form = ReserveReducedForm(
    #         data=request.POST, instance=player_project
    #         )

    #     if player_project_form.is_valid():
    #         # player_project_form.save()
    #         pass

    #     return HttpResponseRedirect(reverse('rota', args=[slug]))


class DeleteSeatingPosition(View):
    """Delete a seating position in a project"""

    def get(self, request, slug, seating_position_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            SeatingPosition, id=seating_position_id
        )  # noqa E501
        sp_player = seating_position.player
        player_project = get_object_or_404(
            PlayerProject, player=sp_player, project=project
        )
        print("DeleteSeatingPosition called")


class ChangePlanStatus(View):
    """Change the status of a seating plan"""

    def get():
        pass
