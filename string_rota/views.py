from django.shortcuts import render


# Create your views here.
def get_projects_list(request):
    return render(request, 'string_rota/projects_list.html')
