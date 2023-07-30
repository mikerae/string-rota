from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import (SeatingPositionForm,
                    SeatingPlanForm,
                    PlayerProjectFormPL,
                    ReserveReducedForm
                    )
from .models import (
    Project,
    Seating_Plan,
    Seating_Position,
    Player,
    Section,
    Player_Project
)


# Create your views here.

def login(request):
    return render(request, 'account/login.html')


class Projects(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Projects, self).dispatch(*args, **kwargs)

    def get(self, request):
        projects = Project.objects.all()

        context = {
            'projects': projects,
            }
        return render(request, 'string_rota/home.html', context)


class Rota(Projects):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Rota, self).dispatch(*args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        print('rota is called')
        projects = Project.objects.all()
        project = get_object_or_404(Project, slug=slug)
        sections = Section.objects.all()
        # check if user is not a player, & is a manager
        try:
            player = get_object_or_404(Player, users_django=request.user.id)
        except Exception as e:
            print(f'You are not logged in as a player. {e}')
            messages.warning(request, f'You are not logged in as a player.')
            return redirect(reverse('projects'))

        section = player.section
        players_in_project = Player_Project.objects.filter(
            project=project
            ).filter(player__section=section)
        # no seating plan?
        try:
            queryset = Seating_Plan.objects.filter(
                project=project,
                )
            seating_plan = get_object_or_404(queryset, section=section.id)
        except Exception as e:
            print(f'There is no Seating Plan for the {project} project. {e}')
            messages.warning(request, f'There is no Seating \
                Plan for the {project} project.')
            return redirect(reverse('projects'))
          
        seating_positions = Seating_Position.objects.filter(
            seating_plan=seating_plan
            ).order_by('position_number')
        res_ply = players_in_project.filter(
            performance_status='RE'
            )
        if not res_ply:
            reserve_player = "Not Allocated"
        else:
            reserve_player = res_ply.get()

        red_ply = players_in_project.filter(
            off_reduced_rep=True
            )
        if not red_ply:
            off_reduced = "Not Allocated"
        else:
            off_reduced = red_ply.get()
        not_available = players_in_project.filter(performance_status='NA')
        repertoire = project.repertoire_name.all()
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        print(f'reserve_player: {reserve_player}')
        print(f'off_reduced: {off_reduced}')

        context = {
            'projects': projects,
            'project': project,
            'seating_plan': seating_plan,
            'seating_positions': seating_positions,
            'players': players_in_project,
            'reserve_player': reserve_player,
            'player_off_reduced_rep': off_reduced,
            'not_available': not_available,
            'repertoire': repertoire,
            'rota_manager': rota_manager,
            'section': section,
            }
        return render(request, 'string_rota/home.html', context)


class AddSeatingPosition(Rota):

    def get(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section

        seating_position_form = SeatingPositionForm()
        player_project_form = PlayerProjectFormPL()

        context = {
                    'projects': projects,
                    'project': project,
                    'section': section,
                    'seating_position_form': seating_position_form,
                    'player_project_form': player_project_form,
                    }

        return render(request, 'string_rota/add_sp.html', context)

    def post(self, request, slug, seating_plan_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position_form = SeatingPositionForm(data=request.POST)
        player_project = get_object_or_404(
            Player_Project,
            player=request.POST.get("player"),
            project=project
            )

        player_project_form = PlayerProjectFormPL(
            data=request.POST, instance=player_project
            )
        seating_plan = get_object_or_404(Seating_Plan, id=seating_plan_id)

        if seating_position_form.is_valid():
            seating_position_form.instance.seating_plan = seating_plan
            seating_position_form.save()

        if player_project_form.is_valid():
            player_project.performance_status = 'PL'
            player_project_form.save()

        return HttpResponseRedirect(reverse('rota', args=[slug]))


class EditSeatingPosition(Rota):

    def get(self, request, slug, seating_position_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            Seating_Position, id=seating_position_id
            )
        sp_player = seating_position.player
        player_project = get_object_or_404(
            Player_Project,
            player=sp_player,
            project=project
            )

        seating_position_form = SeatingPositionForm(instance=seating_position)
        player_project_form = PlayerProjectFormPL(instance=player_project)

        context = {
                    'projects': projects,
                    'project': project,
                    'section': section,
                    'seating_position_form': seating_position_form,
                    'player_project_form': player_project_form,
                    }

        return render(request, 'string_rota/edit_sp.html', context)

    def post(self, request, slug, seating_position_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            Seating_Position, id=seating_position_id
            )
        sp_player = seating_position.player
        player_project = get_object_or_404(
            Player_Project,
            player=sp_player,
            project=project
            )

        seating_position_form = SeatingPositionForm(
            data=request.POST, instance=seating_position
            )
        player_project_form = PlayerProjectFormPL(
            data=request.POST, instance=player_project
            )

        if seating_position_form.is_valid():
            seating_position_form.save()

        if player_project_form.is_valid():
            player_project_form.save()

        return HttpResponseRedirect(reverse('rota', args=[slug]))


class EditPlayerProject(Rota):

    def get(self, request, slug, player_pp_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        player_pp = get_object_or_404(Player, id=player_pp_id)
        player_project = get_object_or_404(
            Player_Project,
            player=player_pp,
            project=project
            )

        player_project_form = EditPlayerProjectForm(instance=player_project)

        context = {
                    'projects': projects,
                    'project': project,
                    'player': sp_player,
                    'section': section,
                    'player_project_form': player_project_form,
                    }

        return render(request, 'string_rota/edit_pp.html', context)

    def post(self, request, slug, player_pp_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        player_pp = get_object_or_404(Player, id=player_pp_id)
        player_project = get_object_or_404(
            Player_Project,
            player=player_pp,
            project=project
            )

        player_project_form = EditPlayerProjectForm(
            data=request.POST, instance=player_project
            )

        if player_project_form.is_valid():
            player_project_form.save()

        return HttpResponseRedirect(reverse('rota', args=[slug]))


class ReserveReduced(Rota):

    def get(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        players_project = Player_Project.objects.filter(
            project=project).filter(player__section=section
                                    )
        print(f'players_project: {players_project}')
        reserve_reduced_form = ReserveReducedForm()

        context = {
                    'projects': projects,
                    'project': project,
                    'section': section,
                    'players_project': players_project,
                    'reserve_reduced_form': reserve_reduced_form
                    }

        return render(request, 'string_rota/reserve_reduced.html', context)

    # def post(self, request, *args, **kwargs):
    #     projects = Project.objects.all()
    #     project = get_object_or_404(projects, slug=slug)
    #     player = get_object_or_404(Player, users_django=request.user.id)
    #     section = player.section
    #     player_pp = get_object_or_404(Player, id=player_pp_id)
    #     player_project = get_object_or_404(
    #         Player_Project,
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

    def get(self, request, slug, seating_position_id, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        seating_position = get_object_or_404(
            Seating_Position, id=seating_position_id
            )
        sp_player = seating_position.player
        player_project = get_object_or_404(
            Player_Project,
            player=sp_player,
            project=project
            )
        print('DeleteSeatingPosition called')


class ChangePlanStatus(View):

    def get():
        pass
