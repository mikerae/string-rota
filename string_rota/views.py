from django.shortcuts import render
from .models import Repertoire
from utilities.get_orch_data import (
    connect_to_worksheet,
    get_repertoire,
    get_players
    )

"""
Utilities to load manually pre-cleaned rsno schedule and player data
from a remote google worksheet into project database.
"""
# Open connection to google worksheet
SHEET = connect_to_worksheet()
# Import data from worksheet
REPERTOIRE_DATA = get_repertoire(SHEET)
PLAYER_DATA = get_players(SHEET)


def load_repertoire_data(DATA, MODULE):
    """ Load project data into project database """
    # for row in WORKSHEET_DATA:
    #     print(row)
    print(DATA[0])


load_repertoire_data(REPERTOIRE_DATA, "")
load_repertoire_data(PLAYER_DATA, "")


# Create your views here.
def get_projects_list(request):
    return render(request, 'string_rota/projects_list.html')
