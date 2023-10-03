"""django_string_rota URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from string_rota.views import login

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("summernote/", include("django_summernote.urls")),
    path("string_rota/", include("string_rota.urls")),
    path("", login, name="login"),
    path("accounts/", include("allauth.urls")),
    path("player_info/", include("player_info.urls")),
]
