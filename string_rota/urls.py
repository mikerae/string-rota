""" Urls for string-rota app """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Projects.as_view(), name="projects"),
    path("<slug:slug>/", views.Rota.as_view(), name="rota"),
    path(
        "add_sp/<slug:slug>/<seating_plan_id>/",
        views.AddSeatingPosition.as_view(),
        name="add_sp",
    ),
    path(
        "edit_sp/<slug:slug>/<seating_position_id>/",
        views.EditSeatingPosition.as_view(),
        name="edit_sp",
    ),
    path(
        "make_reserve/<slug:slug>/<reserve_player_id>",
        views.Reserve.as_view(),
        name="make_reserve",
    ),
    path(
        "reserve/<slug:slug>/",
        views.Reserve.as_view(),
        name="reserve",
    ),
    path(
        "change_plan_status/<slug:slug>/",
        views.ChangePlanStatus.as_view(),
        name="change_plan_status",
    ),
    path(
        "delete_sp/<slug:slug>/<position_id>/",
        views.DeleteSeatingPosition.as_view(),
        name="delete_sp",
    ),
]
