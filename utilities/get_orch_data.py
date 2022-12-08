"""
Get list of file paths for RSNO schedule.csv files. These schedules are
output from the RSNO office in csv format and are dirty.
The utility requires that the current working directory is set in the terminal
to where the files are located.
In this version, there is only one file.
The full file path is returned of the schedule.csv is returned.
"""
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("string_rota_data")

projects = SHEET.worksheet('projects')
projects_raw_data = projects.get_all_records()

players = SHEET.worksheet('players')
players_raw_data = players.get_all_records()

projects_landing_df = pd.DataFrame(projects_raw_data)
players_landing_df = pd.DataFrame(players.get_all_records())

print(projects_landing_df.head())
print(players_landing_df.head())
