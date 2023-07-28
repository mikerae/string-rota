""" A utility module for loading initial RSNO into models """
from datetime import datetime, time
from math import ceil
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from string_rota.models import (
    Repertoire,
    Player,
    Section,
    Session,
    Project,
    )
from utilities.get_orch_data import (
    connect_to_worksheet,
    get_repertoire,
    get_players,
    get_sessions,
    get_projects
    )


def load_rsno_data():
    # Open connection to google worksheet
    SHEET = connect_to_worksheet()
    # Import data from worksheet
    REPERTOIRE_DATA = get_repertoire(SHEET)
    PLAYER_DATA = get_players(SHEET)
    SESSION_DATA = get_sessions(SHEET)
    PROJECT_DATA = get_projects(SHEET)

    def load_repertoire_data(DATA):
        """ Load repertoire data into project database """
        for row in DATA:
            repertoire_row = Repertoire(
                name=row['Repertoire'],
                instrumentation=row['Instrumentation']
                )
            repertoire_row.save()

    def load_player_data(DATA):
        """ Load player data into project database """
        for row in DATA:
            Player.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                annual_nfd_quota=int(row['nd_alloc']),
                section=get_object_or_404(Section, name=row['section'])
                )

    def load_session_data(DATA):
        """
        Load session data into project database.
        Unfortunately, the time format for the imported data
        is 'hr.mn' and is given as a decimal! The following code translates
        time date into datetime.time format
        """
        for row in DATA:

            start_time_h = int(row['start_time'])

            start_time_md = (row['start_time'] - int(row['start_time'])) * 100
            if start_time_md - int(start_time_md) > 0.005:
                start_time_m = ceil(start_time_md)
            elif start_time_md - int(start_time_md) > 0.005:
                start_time_m = int(start_time_md)
            else:
                start_time_m = int(start_time_md)

            end_time_h = int(row['end_time'])

            end_time_md = (row['end_time'] - int(row['end_time'])) * 100
            if end_time_md - int(end_time_md) > 0.005:
                end_time_m = ceil(end_time_md)
            elif end_time_md - int(end_time_md) > 0.005:
                end_time_h = int(end_time_md)
            else:
                end_time_m = int(end_time_md)
            # data_project = row['project']
            Session.objects.create(
                date=datetime.strptime(row['date'], "%a %d %b %y").date(),
                start_time=time(start_time_h, start_time_m),
                end_time=time(end_time_h, end_time_m),
                session_type=row['session_type'],
                project=get_object_or_404(Project, name=row['project'])
                )

    def load_project_data(DATA):
        """ Load project data into project database """
        for row in DATA:
            project_name = row['project']
            slug = slugify(project_name)
            Project.objects.create(
                name=project_name,
                slug=slug,
                )

    # load_repertoire_data(REPERTOIRE_DATA)  # Data already loaded!
    # load_player_data(PLAYER_DATA)  # Data already loaded!
    # load_project_data(PROJECT_DATA)  # Data already loaded!
    # load_session_data(SESSION_DATA)  # Data already loaded!
