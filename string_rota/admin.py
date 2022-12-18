from django.contrib import admin
from .models import (
    Repertoire,
    Section,
    Player,
    # Role,
    # Session,
    # Project,
    # Seating_Position,
    # Seating_Plan,
    # Player_Project
)


# Register your models here.
admin.site.register(Repertoire)
admin.site.register(Section)
admin.site.register(Player)
# admin.site.register(Role)
# admin.site.register(Session)
# admin.site.register(Project)
# admin.site.register(Seating_Position)
# admin.site.register(Seating_Plan)
# admin.site.register(Player_Project)
