from string_rota.models import Repertoire
from utilities.get_orch_data import (
    connect_to_worksheet,
    get_repertoire,
    get_players
    )


def load_data_main():
    # Open connection to google worksheet
    SHEET = connect_to_worksheet()
    # Import data from worksheet
    REPERTOIRE_DATA = get_repertoire(SHEET)
    PLAYER_DATA = get_players(SHEET)

    def load_repertoire_data(DATA):
        """ Load repertoire data into project database """
        for row in DATA:
            repertoire_row = Repertoire(
                rep_name=row['Repertoire'],
                instrumentation=row['Instrumentation']
                )
            repertoire_row.save()

    def load_player_data(DATA):
        """ Load player data into project database """
        print(DATA[0])

    load_repertoire_data(REPERTOIRE_DATA)  # Data already loaded!
    # load_player_data(PLAYER_DATA)
