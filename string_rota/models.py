from django.db import models
from django.conf import settings


class Repertoire(models.Model):
    rep_name = models.CharField(
        max_length=200, unique=True, null=False, blank=False
        )
    instrumentation = models.CharField(max_length=14, null=False, blank=False)

    class Meta:
        verbose_name_plural = "repertoire"

    def __str__(self):
        return self.rep_name


class Section(models.Model):
    section_name = models.CharField(max_length=11, null=False, blank=False)

    def __str__(self):
        return self.section_name


class Player(models.Model):

    player_first_name = models.CharField(max_length=50, unique=True)
    player_last_name = models.CharField(max_length=50, unique=True)
    is_contract = models.BooleanField(
        null=False, blank=False, default=True
        )
    player_notes = models.TextField()
    annual_nfd_quota = models.IntegerField(
        null=False, blank=False, default=0
        )
    nfds_used_to_date = models.IntegerField(
        null=False, blank=False, default=0
        )
    off_reduced_rep_tot = models.IntegerField(
        null=False, blank=False, default=0
        )
    section_name = models.ForeignKey(Section,  on_delete=models.CASCADE)
    users_django_id = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )

    @property
    def player_name(self):
        player_name = Concat(
            'self.player_first_name', Value(' '), 'player_last_name', Value()
            )
        return player_nmae

    def __str__(self):
        return self.player_name

# class Session(models.Model):
#     SESSION_TYPE_CHOICES = [
#         ('REH', 'Rehersal'),
#         ('CON', 'Concert'),
#         ('REC', 'Recording'),
#     ]
#     session_date = models.DateField(
#         auto_now=False, auto_now_add=False, null=False, blank=False
#         )
#     session_start_time = models.DateTimeField(null=False, blank=False)
#     session_end_time = models.DateTimeField(null=False, blank=False)
#     session_type = models.CharField(
#         max_length=3, choices=SESSION_TYPE_CHOICES, default='REH'
#         )
#     repertoire_id = models.ForeignKey(Repertoire, on_delete=models.RESTRICT)

#     def __str__(self):
#         return self.session_type


# class Project(models.Model):
#     project_name = models.CharField(max_length=200, null=False, blank=False)
#     player = models.ManyToManyField(Player, through='player_project')
#     repertoire_name = models.ManyToManyField(Repertoire)
#     seating_plan = models.ManyToManyField(
#             'Seating_Position', through='Seating_Plan'
#         )
#     session = models.ForeignKey(Session, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.project_name


# class Seating_Position(models.Model):
#     position_number = models.IntegerField()
#     seating_plan = models.ForeignKey(
#         'Seating_Plan', on_delete=models.CASCADE, related_name='plan',
#         )
#     player_id = models.ForeignKey(
#         Player, on_delete=models.CASCADE
#         )
#     section_id = models.ForeignKey(
#         Section, on_delete=models.CASCADE
#         )

#     def __str__(self):
#         return self.position_number


# class Seating_Plan(models.Model):
#     is_published = models.BooleanField(default=False)
#     project_id = models.ForeignKey(
#         Project, on_delete=models.CASCADE, related_name='seating_plans',
#         )
#     section_name = models.ForeignKey(Section, on_delete=models.CASCADE)
#     seating_position = models.ForeignKey(
#         Seating_Position, on_delete=models.CASCADE, related_name='postition',
#         )
#     player = models.ManyToManyField(Player, through='seating_position',)

#     def __str__(self):
#         return self.project_id


# class Player_Project(models.Model):
#     PERFORMANCE_STATUS_CHOICES = [
#         ('PL', 'Playing'),
#         ('RE', 'Reserve'),
#         ('NA', 'Not Available'),
#     ]
#     performance_status = models.CharField(
#         max_length=2,
#         null=False,
#         blank=False,
#         choices=PERFORMANCE_STATUS_CHOICES,
#         default='PL'
#         )
#     off_reduced_rep = models.BooleanField(
#         null=False, default=False
#         )
#     trialist = models.BooleanField(null=False, blank=False, default=False)
#     guest_principal = models.BooleanField(
#         null=False, default=False
#         )
#     project_id = models.ForeignKey(
#         Project,  on_delete=models.CASCADE
#         )
#     player_id = models.ForeignKey(
#         Player,  on_delete=models.CASCADE
#         )

#     def __str__(self):
#         return self.performance_status
