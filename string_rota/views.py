from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import SeatingPositionForm, SeatingPlanForm, PlayerProjectForm
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
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        sections = Section.objects.all()
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        players_in_project = Player_Project.objects.filter(
            project=project
            ).filter(player__section=section)
        queryset = Seating_Plan.objects.filter(
            project=project,
            )
        seating_plan = get_object_or_404(queryset, section=section.id)
        seating_positions = Seating_Position.objects.filter(
            seating_plan=seating_plan
            ).order_by('position_number')
        res_ply = players_in_project.filter(
            performance_status='RE'
            )
        if not res_ply:
            reserve_player = "Not Allocated"
        else:
            reserve_player = res_ply.get().player

        red_ply = players_in_project.filter(
            off_reduced_rep=True
            )
        if not red_ply:
            off_reduced = "Not Allocated"
        else:
            off_reduced = red_ply.get().player
        not_available = players_in_project.filter(performance_status='NA')
        repertoire = project.repertoire_name.all()
        rota_manager = request.user.groups.filter(name="Rota_Manager")

        seating_position_form = SeatingPositionForm()
        seating_plan_form = SeatingPlanForm(instance=seating_plan)
        player_project_form = PlayerProjectForm()

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
            'seating_position_form': seating_position_form,
            'seating_plan_form': seating_plan_form,
            'player_project_form': player_project_form,
            }
        return render(request, 'string_rota/home.html', context)

    def post(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        player = get_object_or_404(Player, users_django=request.user.id)
        section = player.section
        queryset = Seating_Plan.objects.filter(
            project=project,
            )
        seating_plan = get_object_or_404(queryset, section=section.id)

        seating_position_form = SeatingPositionForm(data=request.POST)
        seating_plan_form = SeatingPlanForm(
            data=request.POST, instance=seating_plan
            )
        player_project = get_object_or_404(
            Player_Project,
            player=request.POST.get("player"),
            project=project
            )
        player_project_form = PlayerProjectForm(
            data=request.POST, instance=player_project
            )

        if seating_position_form.is_valid():
            seating_position_form.instance.seating_plan = seating_plan
            seating_position_form.save()
        else:
            seating_position_form = SeatingPositionForm()

        if seating_plan_form.is_valid():
            seating_plan_form.save()
        else:
            seating_plan_form()

        if player_project_form.is_valid():
            player_project_form.save()

        else:
            player_project_form = player_project_form()

        return HttpResponseRedirect(reverse('rota', args=[slug]))


# class UpdateSeatingPosition(View):

#     def post(self, request, slug, *args, **kwargs):
#         pass
