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
        "reserve/<slug:slug>/",
        views.Reserve.as_view(),
        name="reserve",
    ),
    path(
        "delete_sp/<slug:slug>/<position_id>/",
        views.DeleteSeatingPosition.as_view(),
        name="delete_sp",
    ),
    path(
        "<slug:slug>/<seating_plan_id>/",
        views.ToggleSeatingPlanStatus.as_view(),
        name="toggle_seating_plan_status",
    ),
]
