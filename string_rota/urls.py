from . import views
from django.urls import path

urlpatterns = [
    path('', views.Projects.as_view(), name='projects'),
    path('<slug:slug>/', views.Rota.as_view(), name='rota'),
    path('add_sp/<slug:slug>/<seating_plan_id>/',
         views.AddSeatingPosition.as_view(),
         name='add_sp'
         ),
    path('edit_sp/<slug:slug>/<seating_position_id>/',
         views.EditSeatingPosition.as_view(),
         name='edit_sp'
         ),
    path('change_plan_status/<slug:slug>/',
         views.ChangePlanStatus.as_view(),
         name='change_plan_status'
         ),
    path('delete_sp/<seating_position_id>/',
         views.DeleteSeatingPosition.as_view(),
         name='delete_sp'
         ),
    ]
