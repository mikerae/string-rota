""" Most internal set-up records were manually, since only
    basic CRUD functionality is needed for the CI project assesment.
    Automatically creating projects and all related table records is
    beyond the scope of this version of the project.
    The Player_Project table needed to be populated with all projects,
    and all players in order for a seating plan to be populated.
    Initialy all players are set to be 'Not Available' for all projects.

"""
from string_rota.models import (
    Player,
    Project,
    Player_Project,
    )


def setup_tables():

    def setup_player_project():
        """
        Creates a player_project record for each project,
        and each player.
        """
        projects = Project.objects.all()
        players = Player.objects.all()
        for project in projects:
            for player in players:
                Player_Project.objects.create(
                    project=Project.objects.get(id=project.id),
                    player=Player.objects.get(id=player.id)
                )

    # setup_player_project()  # Data already loaded!
