"""
Utilities to load manually pre-cleaned rsno schedule and player data
from a remote google worksheet into project database.
This data simulates a live api connection to RSNO servers.
This script is to be used once, only.
Subsequent data loading is to be done through the use of fixtures.
"""
import os
import django

if __name__ == '__main__':
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "django_string_rota.settings"
        )
    django.setup()
    from utilities.load_rsno_data import load_rsno_data
    from utilities.setup_tables import setup_tables

    load_rsno_data()
    setup_tables()
