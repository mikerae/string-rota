# pylint: disable=no-member
"""
Utilities to ensure correct background records exist, and to validate CRUD
actions.
"""
from .models import PlayerProject, Player, Project, SeatingPlan, Section


def check_player_project():
    """
    Check for existance of player_project record for each player and
    projects. If not found, creates one.
    """
    print('checking player_project records...')
    players = Player.objects.all()
    projects = Project.objects.all()
    for project in projects:
        for player in players:
            player_in_project = PlayerProject.objects.filter(project=project
                                                             ).filter(
                                                                player=player)
            if not player_in_project:
                PlayerProject.objects.create(
                    project=project,
                    player=player,
                )
                print(f'record created for  {project} - {player}')
            elif player_in_project.count() != 1:
                print(f'found {player_in_project.count()} records \
                    for {project} - {player}')

    print('check for player_project records completed')


def check_seating_plan():
    """
    Check for existance of seating_plan for each project and section.
    If not found, creates one.
    """
    print('checking check_seating_plan records...')
    projects = Project.objects.all()
    seating_plans = SeatingPlan.objects.all()
    sections = Section.objects.all()
    for project in projects:
        for section in sections:
            seating_plan = seating_plans.filter(
                                                project=project
                                                ).filter(
                                                section=section)
            if not seating_plan:
                SeatingPlan.objects.create(
                    project=project,
                    section=section,
                )
    print('check for seating plan records completed')
