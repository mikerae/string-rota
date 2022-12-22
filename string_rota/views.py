from django.shortcuts import render, redirect, get_object_or_404
from .models import Project


# Create your views here.
def log_in(request):
    return render(request, 'string_rota/log_in.html')


def player(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'string_rota/player.html', context)


def error_404(request):
    return render(request, 'string_rota/error-404.html')
