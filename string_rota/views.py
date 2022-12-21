from django.shortcuts import render


# Create your views here.
def log_in(request):
    return render(request, 'string_rota/log_in.html')


def player(request):
    return render(request, 'string_rota/player.html')


def error_404(request):
    return render(request, 'string_rota/error-404.html')
