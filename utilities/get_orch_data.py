"""
Get raw data for RSNO Strings Player List (with Annual Free Day Allocation),
and sample Project Data for four weeks.

"""
import gspread
from google.oauth2.service_account import Credentials


def connect_to_worksheet():
    """
    Coonect to Google Drive Worksheet conntaining
    sample data for 4 weeks of projects, and string player
    Annual Natural Free Day Allocation.

    """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("string_rota_data")

    return SHEET


def get_repertoire(SHEET):
    """
    Import sample data for 4 weeks of RSNO projects
    """
    # print('get_repertoire is called')
    repertoire = SHEET.worksheet('repertoire')
    # print(f'repertoire: {repertoire}')
    return repertoire.get_all_records()


def get_players(SHEET):
    """
    Import sample data for RSNO String Player
    Annual Natural Free Day Allocation
    """
    # print('get_players is called')
    players = SHEET.worksheet('players')
    # print(f'players: {players}')
    return players.get_all_records()


def get_sessions(SHEET):
    """
    Import sample data for RSNO Project Sessions
    """
    # print('get_sessions is called')
    sessions = SHEET.worksheet('sessions')
    return sessions.get_all_records()


def get_projects(SHEET):
    """
    Import sample data for RSNO Project Sessions
    """
    # print('get_projects is called')
    projects = SHEET.worksheet('projects')
    return projects.get_all_records()
