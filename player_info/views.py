# pylint: disable=no-member
""" Views for Player Info app """
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from string_rota.utilities import (
    get_player,
    get_section,
)


class Register(View):
    """Register view shows a list of players currently on the rota
    list for a given section, and shows which are registered.
    It presents a registration form which can be populated with a
    chosen unregistered player.
    On form submission it creates a user with giben username and password
    via allauth, and creates a linked Player record.
    Player-Project records are then checked and new records are then
    created for this player.
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Register, self).dispatch(*args, **kwargs)

    def get(self, request):
        """Display list of players currently on the rota
        list for a given section, and shows which are registered.
        Presents a registration form which can be populated with a
        chosen unregistered player."""

        player = get_player(request)
        section = get_section(player)
        office = request.user.groups.filter(name="Office")
        rota_manager = request.user.groups.filter(name="Rota_Manager")

        template = "player_info/register.html"

        context = {
            "section": section,
            "office": office,
            "rota_manager": rota_manager,
        }

        return render(request, template, context)
