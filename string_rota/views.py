from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
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
            )
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
        print(request.user.groups.all())

        context = {
            'projects': projects,
            'project': project,
            'seating_plan': seating_plan,
            'seating_positions': seating_positions,
            'players': players_in_project,
            'reserve_player': reserve_player,
            'player_off_reduced_rep': off_reduced,
            'not_available': not_available,
            'repertoire': repertoire
            }
        return render(request, 'string_rota/home.html', context)

    def post(self, request, slug, *args, **kwargs):
        projects = Project.objects.all()
        project = get_object_or_404(projects, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        rota_form = RotaForm(data=request.POST)

        if rota_form.is_valid():
            rota_form.instance.email = request.user.email
            rota_form.instance.name = request.user.username
            # rota = rota_form.save(commit=False)
            # Add relative field actions
            #
            # rota.save()
            messages.success(
                request, 'Your rota has been posted!'
                )
        else:
            rota_form = RotaForm()

        return render(
            request,
            'home.html',
            {
                # "post": post,
                # "comments": comments,
                # "commented": True,
                # "liked": liked,
                # "rota_form": CommentForm(),
            },
        )
