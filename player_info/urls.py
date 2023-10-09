""" Urls for player_info app """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Register.as_view(), name="register"),
    path("<section_id>/", views.Register.as_view(), name="register_office"),
]
