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
    #     path('edit_pp/<slug:slug>/<player_pp_id>',
    #          views.EditPlayerProject.as_view(),
    #          name='edit_pp'
    #          ),
    path(
        "reserve_reduced/<slug:slug>",
        views.ReserveReduced.as_view(),
        name="reserve_reduced",
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
