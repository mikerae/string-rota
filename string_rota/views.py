from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Project, Seating_Plan


# Create your views here.

def log_in(request):
    return render(request, 'string_rota/log_in.html')


def home(request):
    projects = Project.objects.all()
    current_project = Project.objects.all()[0]
    current_project_seating_plans = Seating_Plan.objects.filter(
        project=current_project
        )
    context = {
        'projects': projects,
        'current_project': current_project,
        'seating_plans': current_project_seating_plans
        }
    return render(request, 'string_rota/home.html', context)
