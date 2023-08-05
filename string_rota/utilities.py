# pylint: disable=no-member
"""
Utilities to ensure correct background records exist, and to validate CRUD
actions.
"""
from django.shortcuts import get_object_or_404
from .models import (
    PlayerProject,
    Player,
    Project,
    SeatingPlan,
    Section,
    SeatingPosition,
)


def check_player_project():
    """
    Check for existance of player_project record for each player and
    projects. If not found, creates one.
    """
    print("checking player_project records...")
    players = Player.objects.all()
    projects = Project.objects.all()
    for project in projects:
        for player in players:
            player_in_project = PlayerProject.objects.filter(
                project=project
            ).filter(  # noqa E501
                player=player
            )
            if not player_in_project:
                PlayerProject.objects.create(
                    project=project,
                    player=player,
                )
                print(f"record created for  {project} - {player}")
            elif player_in_project.count() != 1:
                print(
                    f"Error: found {player_in_project.count()} records \
                    for {project} - {player}"
                )

    print("check for player_project records completed")


def check_seating_plan():
    """
    Check for existance of seating_plan for each project and section.
    If not found, creates one.
    """
    print("checking check_seating_plan records...")
    projects = Project.objects.all()
    seating_plans = SeatingPlan.objects.all()
    sections = Section.objects.all()
    for project in projects:
        for section in sections:
            seating_plan = seating_plans.filter(project=project).filter(
                section=section
            )  # noqa E501
            if not seating_plan:
                SeatingPlan.objects.create(
                    project=project,
                    section=section,
                )
                print(f"seating plan created for  {project} - {section}")
    print("check for seating plan records completed")


def get_reserve_vars(request, slug):
    """
    Returns the current Player_Project, section, seating plan,
    project and available_players objects, for given args. It assumes Project,
    Player SeatingPlan models are available.
    """
    project = get_project(slug)
    player = get_player(request)
    section = get_section(player)
    seating_plan = get_seating_plan(project, section)
    players = get_players(section)
    not_playing_in_playerproject = get_not_playing_in_playerproject(
        players, seating_plan, project
    )
    return (project, section, seating_plan, not_playing_in_playerproject)  # noqa E501


def get_project(slug):
    """Returns project given project slug"""
    project = get_object_or_404(Project, slug=slug)
    return project


def get_player(request):
    """Returns player given request"""
    player = get_object_or_404(Player, users_django=request.user.id)
    return player


def get_players(section):
    """Returns players given section"""
    players = Player.objects.filter(section=section)
    return players


def get_section(player):
    """Returns section given player"""
    section = player.section
    return section


def get_seating_plan(project, section):
    """Returns seating_plan for given project"""
    seating_plan = get_object_or_404(
        SeatingPlan, project=project, section=section
    )  # noqa E501
    return seating_plan


def get_not_available_players(seating_plan, players):
    """
    Returns players in a project and section not
    allocated a seating position
    """
    allocated_players = seating_plan.players.all()
    not_available_players = players.exclude(pk__in=allocated_players)
    return not_available_players


def get_seating_positions(seating_plan):
    """
    Returns an ordered queryset of seating positions
    for a given project and section
    """
    seating_positions = SeatingPosition.objects.filter(
        seating_plan=seating_plan
    ).order_by("position_number")
    return seating_positions


def get_not_playing_in_playerproject(players, seating_plan, project):
    """
    Returns player_project records  for  given project,
    seating_plan and players
    """
    not_available_players = get_not_available_players(seating_plan, players)

    not_playing_in_playerproject = PlayerProject.objects.filter(
        project=project
    ).filter(  # noqa E501
        player__in=not_available_players
    )
    return not_playing_in_playerproject


def get_playing_in_playerproject(seating_plan, project):
    """
    Returns player_project records  given section players
    who are playing in tha given project
    """
    allocated_players = seating_plan.players.all()

    playing_in_playerproject = PlayerProject.objects.filter(
        project=project
    ).filter(  # noqa E501
        player__in=allocated_players
    )
    return playing_in_playerproject


def get_all_playerproject(seating_plan, project):
    """
    Returns player_project records  for  given project and
    seating_plan
    """
    section = seating_plan.section
    players_in_section = get_players(section)

    all_playerproject = PlayerProject.objects.filter(
        project=project
    ).filter(  # noqa E501
        player__in=players_in_section
    )
    return all_playerproject
