# pylint: disable=no-member
""" Views for Player Info app """
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from string_rota.models import Project, Player
from string_rota.utilities import (
    get_player,
    get_section,
    get_players,
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
        projects = Project.objects.all()
        section_players = get_players(section)
        unregistered_players = section_players.filter(users_django__isnull=True)  # noqa
        if unregistered_players:
            create_user_form = UserCreationForm()

            template = "player_info/register.html"

            context = {
                "section": section,
                "office": office,
                "rota_manager": rota_manager,
                "projects": projects,
                "unregistered_players": unregistered_players,
                "create_user_form": create_user_form,
            }

            return render(request, template, context)
        else:
            messages.info(
                request,
                f"All players in the  {section} section are registered and have access to the String Rota app",  # noqa
            )
            return HttpResponseRedirect(
                reverse(
                    "home",
                )
            )

    def post(
        self,
        request,
    ):
        """Create user and link user to Player record"""

        player_id = request.POST["player_id"]
        player = get_player(request)
        section = get_section(player)
        office = request.user.groups.filter(name="Office")
        rota_manager = request.user.groups.filter(name="Rota_Manager")
        projects = Project.objects.all()
        registered_player = get_object_or_404(Player, id=player_id)
        section_players = get_players(section)
        unregistered_players = section_players.filter(users_django__isnull=True)  # noqa

        create_user_form = UserCreationForm(request.POST)
        if create_user_form.is_valid():
            username = create_user_form.cleaned_data["username"]
            password = create_user_form.cleaned_data["password1"]
            new_user = create_user_form.save()
            new_user.first_name = registered_player.first_name
            new_user.last_name = registered_player.last_name
            group = Group.objects.get(name="Player")
            new_user.groups.add(group)
            new_user.save()

            # Link new user to Player record
            registered_player.users_django = new_user
            registered_player.save()

            messages.success(
                request, f"{registered_player} has been registered"
            )  # noqa
            messages.warning(
                request,
                f"Please make a note of {registered_player}'s username: {username} and password: {password}",  # noqa
            )
            return HttpResponseRedirect(
                reverse(
                    "home",
                )
            )
        else:
            print("register form not valid")
            print(f"errors:  {create_user_form.error_messages}")
            template = "player_info/register.html"
            context = {
                "section": section,
                "office": office,
                "rota_manager": rota_manager,
                "projects": projects,
                "unregistered_players": unregistered_players,
                "create_user_form": create_user_form,
                "create_user_form_errors": create_user_form.error_messages,
            }
            return render(request, template, context)
