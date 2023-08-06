"""
Get raw data for RSNO Strings Player List (with Annual Free Day Allocation),
and sample Project Data for four weeks.

"""
import gspread
from google.oauth2.service_account import Credentials


def connect_to_worksheet():
    """
    Connect to Google Drive Worksheet conntaining
    sample data for 4 weeks of projects, and string player
    Annual Natural Free Day Allocation.

    """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("string_rota_data")

    return SHEET


def get_repertoire(SHEET):
    """
    Import sample data for 4 weeks of RSNO projects
    """
    repertoire = SHEET.worksheet("repertoire")
    return repertoire.get_all_records()


def get_players(SHEET):
    """
    Import sample data for RSNO String Player
    Annual Natural Free Day Allocation
    """
    players = SHEET.worksheet("players")
    return players.get_all_records()


def get_sessions(SHEET):
    """
    Import sample data for RSNO Project Sessions
    """
    sessions = SHEET.worksheet("sessions")
    return sessions.get_all_records()


def get_projects(SHEET):
    """
    Import sample data for RSNO Project Sessions
    """
    projects = SHEET.worksheet("projects")
    return projects.get_all_records()
