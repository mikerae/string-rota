from . import views
from django.urls import path

urlpatterns = [
    path('', views.Projects.as_view(), name='projects'),
    path('<slug:slug>/', views.Rota.as_view(), name='rota'),
    path(
        '<slug:slug>/manage_rota/',
        views.ManageRota.as_view(),
        name='manage_rota'
        ),
]
