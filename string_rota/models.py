from django.db import models
from django.conf import settings


class Repertoire(models.Model):
    name = models.CharField(
        max_length=200, null=False, blank=False
        )
    instrumentation = models.CharField(max_length=14, null=False, blank=False)

    class Meta:
        verbose_name_plural = "repertoire"

    def __str__(self):
        return f"{self.name} - {self.instrumentation}"


class Section(models.Model):
    name = models.CharField(max_length=11, null=False, blank=False)
    players = models.ManyToManyField('Player', related_name='stg_section')

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_contract = models.BooleanField(
        null=False, blank=False, default=True
        )
    notes = models.TextField(null=True, blank=True)
    annual_nfd_quota = models.IntegerField(
        null=False, blank=False, default=0
        )
    nfds_used_to_date = models.IntegerField(
        null=False, blank=False, default=0
        )
    off_reduced_rep_tot = models.IntegerField(
        null=False, blank=False, default=0
        )
    section = models.ForeignKey(Section,  on_delete=models.CASCADE)
    users_django = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Session(models.Model):
    SESSION_TYPE_CHOICES = [
        ('REH', 'Rehersal'),
        ('CON', 'Concert'),
        ('REC', 'Recording'),
    ]
    date = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=False
        )
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
        )
    end_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
        )
    session_type = models.CharField(
        max_length=3, choices=SESSION_TYPE_CHOICES, default='REH'
        )
    repertoire = models.ManyToManyField(
        Repertoire
        )
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_time} / {self.date} / {self.project}"


class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    player = models.ManyToManyField(Player, through='player_project')
    repertoire_name = models.ManyToManyField(Repertoire)
    seating_plan = models.ManyToManyField(
        'Seating_Plan',
        related_name='plan_seating',
        )
    sessions = models.ManyToManyField(Session, related_name='session')

    def __str__(self):
        return self.name


class Seating_Position(models.Model):
    position_number = models.IntegerField()
    seating_plan = models.ForeignKey(
        'Seating_Plan',
        null=True,
        on_delete=models.CASCADE
        )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seating_plan} {self.player} {self.position_number}'


class Seating_Plan(models.Model):
    PLAN_STATUS_CHOICES = [
        ('D', 'Draft'),
        ('P', 'Published')
        ]
    plan_status = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=PLAN_STATUS_CHOICES,
        default='D'
        )
    project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.CASCADE,
        related_name='project_plan'
        )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    player = models.ManyToManyField(
        Player,
        through='Seating_Position',
        through_fields=('seating_plan', 'player')
        )

    def __str__(self):
        return f'{self.section} {self.project}'


class Player_Project(models.Model):
    PERFORMANCE_STATUS_CHOICES = [
        ('PL', 'Playing'),
        ('RE', 'Reserve'),
        ('NA', 'Not Available'),
    ]
    performance_status = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=PERFORMANCE_STATUS_CHOICES,
        default='NA'
        )
    off_reduced_rep = models.BooleanField(
        null=False, default=False
        )
    trialist = models.BooleanField(null=False, blank=False, default=False)
    guest_principal = models.BooleanField(
        null=False, default=False
        )
    project = models.ForeignKey(
        Project,  on_delete=models.CASCADE
        )
    player = models.ForeignKey(
        Player,  on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.player} {self.project}'
