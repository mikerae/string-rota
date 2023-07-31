""" Admin Settings for string-rota """
from django.contrib import admin
from .models import (
    Repertoire,
    Section,
    Player,
    Session,
    Project,
    SeatingPosition,
    SeatingPlan,
    PlayerProject
)


# Register your models here.
admin.site.register(Repertoire)
admin.site.register(Section)
admin.site.register(Player)
admin.site.register(Session)
admin.site.register(Project)
admin.site.register(SeatingPosition)
admin.site.register(SeatingPlan)
admin.site.register(PlayerProject)
