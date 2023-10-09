""" Urls for string-rota app """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("<slug:slug>/", views.Rota.as_view(), name="rota"),
    path(
        "<slug:slug>/<section_id>/", views.Rota.as_view(), name="rota_office"
    ),  # noqa E501
    path(
        "reserve/<slug:slug>/",
        views.Reserve.as_view(),
        name="reserve",
    ),
    path(
        "reserve/<slug:slug>/<section_id>/",
        views.Reserve.as_view(),
        name="reserve_office",
    ),
    path(
        "add_sp/<slug:slug>/<seating_plan_id>/",
        views.AddSeatingPosition.as_view(),
        name="add_sp",
    ),
    path(
        "add_sp/<slug:slug>/<seating_plan_id>/<section_id>/",
        views.AddSeatingPosition.as_view(),
        name="add_sp_office",
    ),
    path(
        "edit_sp/<slug:slug>/<seating_position_id>/",
        views.EditSeatingPosition.as_view(),
        name="edit_sp",
    ),
    path(
        "edit_sp/<slug:slug>/<seating_position_id>/<section_id>/",
        views.EditSeatingPosition.as_view(),
        name="edit_sp_office",
    ),
    path(
        "delete_sp/<slug:slug>/<position_id>/",
        views.DeleteSeatingPosition.as_view(),
        name="delete_sp",
    ),
    path(
        "delete_sp/<slug:slug>/<position_id>/<section_id>/",
        views.DeleteSeatingPosition.as_view(),
        name="delete_sp_office",
    ),
    path(
        "toggle/<slug:slug>/<seating_plan_id>/",
        views.ToggleSeatingPlanStatus.as_view(),
        name="toggle_seating_plan_status",
    ),
    path(
        "toggle/<slug:slug>/<seating_plan_id>/<section_id>/",
        views.ToggleSeatingPlanStatus.as_view(),
        name="toggle_seating_plan_status_office",
    ),
]
