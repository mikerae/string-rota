from . import views
from django.urls import path

urlpatterns = [
    path('', views.Projects.as_view(), name='projects'),
    path('<slug:slug>/', views.Rota.as_view(), name='rota'),
    path('editsp/<seating_position_id>/',
         views.EditSeatingPosition.as_view(),
         name='editsp'
         )
]
