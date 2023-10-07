"""django_string_rota URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import PasswordChangeView

from string_rota.views import login


class CustomPasswordChangeView(PasswordChangeView):
    """Redirect url for successfull password change"""

    success_url = "/string_rota"


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("summernote/", include("django_summernote.urls")),
    path("string_rota/", include("string_rota.urls")),
    path("", login, name="login"),
    re_path(
        r"^accounts/password/change/$",
        CustomPasswordChangeView.as_view(),
        name="account_password_change",
    ),
    path("accounts/", include("allauth.urls")),
    path("player_info/", include("player_info.urls")),
]
