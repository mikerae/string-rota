from django.shortcuts import render


# Create your views here.
def log_in(request):
    return render(request, 'string_rota/log_in.html')
