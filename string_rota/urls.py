from . import views
from django.urls import path

urlpatterns = [
    path('', views.Vln1.as_view(), name='vln1')
]
