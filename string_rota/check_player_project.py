"""
Utility to check for existance of player_project record for each player and
projects. If not found, it creates one.
"""
from django.shortcuts import get_object_or_404
from string_rota.models import Player_Project, Player, Project


def check_player_project():
    """ check for existance of player_project record for each player and
    projects. If not found, it creates one.
    """
    print('checking player_project records...')
    players = Player.objects.all()
    projects = Project.objects.all()
    for project in projects:
        for player in players:
            player_in_project = Player_Project.objects.filter(project=project
                                                              ).filter(
                                                                player=player)
            if not player_in_project:
                Player_Project.objects.create(
                    project=project,
                    player=player,
                )
                print(f'record created for  {project} - {player}')
    print('check for player_project records completed')
    return
