"""
Utilities to clean dirty rsno schedule and player dataframes
into a format usable by the 'create_projects.py' module.
"""
import pandas as pd
import numpy as np
import janitor
from get_orch_data import connect_to_worksheet, get_projects, get_players

# Open connection to google worksheet
SHEET = connect_to_worksheet()
# Import data from worksheet
PROJECTS_RAW_DATA = get_projects(SHEET)
PLAYERS_RAW_DATA = get_players(SHEET)

# Load data into pandas dataframes
projects_landing_df = pd.DataFrame(PROJECTS_RAW_DATA)
players_landing_df = pd.DataFrame(PLAYERS_RAW_DATA)

# print(projects_landing_df.head())
print(players_landing_df.head())
