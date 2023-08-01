""" Models for string-rota app """
from django.db import models
from django.conf import settings


class Repertoire(models.Model):
    """Project Repertoire"""

    name = models.CharField(max_length=200, null=False, blank=False)
    instrumentation = models.CharField(max_length=14, null=False, blank=False)

    class Meta:
        """Customisation of Repertoire model"""

        verbose_name_plural = "repertoire"

    def __str__(self):
        return f"{self.name} - {self.instrumentation}"


class Section(models.Model):
    """Orchestral String Section model"""

    name = models.CharField(max_length=11, null=False, blank=False)
    players = models.ManyToManyField("Player", related_name="sections")

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    """Orchestral Player model"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_contract = models.BooleanField(null=False, blank=False, default=True)
    notes = models.TextField(null=True, blank=True)
    annual_nfd_quota = models.IntegerField(null=False, blank=False, default=0)
    nfds_used_to_date = models.IntegerField(null=False, blank=False, default=0)
    off_reduced_rep_tot = models.IntegerField(
        null=False, blank=False, default=0
    )  # noqa E501
    section = models.ForeignKey(Section, on_delete=models.RESTRICT)
    users_django = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Session(models.Model):
    """Session events for Project"""

    SESSION_TYPE_CHOICES = [
        ("REH", "Rehersal"),
        ("CON", "Concert"),
        ("REC", "Recording"),
    ]
    date = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=False
    )  # noqa E501
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
    )
    end_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=False, blank=False
    )
    session_type = models.CharField(
        max_length=3, choices=SESSION_TYPE_CHOICES, default="REH"
    )
    repertoire = models.ManyToManyField(Repertoire, related_name="sessions")
    project = models.ForeignKey(
        "Project", null=True, on_delete=models.RESTRICT
    )  # noqa E501

    def __str__(self):
        return f"{self.start_time} / {self.date} / {self.project}"


class Project(models.Model):
    """Orchestral Projects"""

    name = models.CharField(
        max_length=200, null=False, blank=False, unique=True
    )  # noqa E501
    slug = models.SlugField(max_length=200, unique=True)
    players = models.ManyToManyField(
        Player, through="PlayerProject", through_fields=("project", "player")
    )
    repertoire_name = models.ManyToManyField(
        Repertoire, related_name="repertoire"
    )  # noqa E501
    seating_plan = models.ManyToManyField(
        "SeatingPlan",
        related_name="project_s_plan",
    )
    sessions = models.ManyToManyField(Session, related_name="project_sessions")

    def __str__(self):
        return str(self.name)


class SeatingPosition(models.Model):
    """A Players seating position in a Project"""

    position_number = models.PositiveIntegerField()
    seating_plan = models.ForeignKey(
        "SeatingPlan", null=True, on_delete=models.RESTRICT
    )
    player = models.ForeignKey(Player, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.seating_plan} {self.player} {self.position_number}"


class SeatingPlan(models.Model):
    """The seating plan for a Project"""

    PLAN_STATUS_CHOICES = [("D", "Draft"), ("P", "Published")]
    plan_status = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=PLAN_STATUS_CHOICES,
        default="D",  # noqa E501
    )
    project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.CASCADE,
        related_name="s_plans_project",  # noqa E501
    )
    section = models.ForeignKey(Section, on_delete=models.RESTRICT)
    players = models.ManyToManyField(
        Player,
        related_name="s_plans_players",
        through="SeatingPosition",
        through_fields=("seating_plan", "player"),
    )

    def __str__(self):
        return f"{self.section} {self.project}"


class PlayerProject(models.Model):
    """A historical record of a player's data for a particular project"""

    PERFORMANCE_STATUS_CHOICES = [
        ("PL", "Playing"),
        ("RE", "Reserve"),
        ("NA", "Not Available"),
    ]
    performance_status = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=PERFORMANCE_STATUS_CHOICES,
        default="NA",
    )
    off_reduced_rep = models.BooleanField(
        null=False, blank=False, default=False
    )  # noqa E501
    trialist = models.BooleanField(null=False, blank=False, default=False)
    guest_principal = models.BooleanField(
        null=False, blank=False, default=False
    )  # noqa E501
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)
    player = models.ForeignKey(Player, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.player} {self.project}"
