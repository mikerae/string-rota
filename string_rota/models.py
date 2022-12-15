from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.project_name


class Repertoire(models.Model):
    rep_name = models.CharField(
        max_length=200, unique=True, null=False, blank=False
        )
    instrumentation = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        return self.rep_name


class ProjectRepertoire(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
    )
    repertoire = models.ManyToManyField(
        Repertoire,
    )

    def __str__(self):
        return self.project.project_name

# class Player_Project(models.Model):
#     PERFORMANCE_STATUS_CHOICES = (
#         (PL, 'Playing'),
#         (RE, 'Reserve'),
#         (NA, 'Not Available')
#     )

#     performance_status = models.CharField(
#         max_lenght=2,
#         null=False,
#         none=False,
#         choices=PERFORMANCE_STATUS_CHOICES,
#         default=PL
#         )
#     off_reduced_rep = models.BooleanField(
#         null=False, blank=False, default=False
#         )

#     def nfd_this_project():
#         pass
#     nfd_this_project = property(_nfd_this_project)
#     trialist = models.BooleanField(null=False, blank=False, default=False)
#     guest_principal = models.BooleanField(
#         null=False, none=False, default=False
#         )


# class Player(models.Model):

#     VLN1 = 'VLN1'
#     VLN2 = 'VLN2'
#     VLA = 'VLA'
#     VLC = 'VLC'
#     DB = 'DB'

#     SECTION_CHOICES = [
#         (VLN1, 'First Violin'),
#         (VLN2, 'Second Violin'),
#         (VLA, 'Viola'),
#         (VLC, 'Cello'),
#         (DB, 'Double Bass')
#     ]

#     project = models.ManyToManyField(project, through=player_project)
#     player_name = CharField(max_length=50, unique=True)
#     is_contract = models.BooleanField(
#         null=False, blank=False, default=True
#         )
#     player_notes = models.TextField()
#     annual_nfd_quota = models.IntegerField(null=False, blank=False)
#     nfds_used_to_date = models.IntegerField()

#     def _nfds_over_quota(self.annual_nfd_quota, self.nfds_used_to_date):
#         return self.annual_nfd_quota - self.fds_used_to_date

#     nfds_over_quota = property(_nfds_over_quota)
#     off_reduced_rep_tot = models.IntegerField()
#     section = models.CharField(
#         max_length=4, choices=SECTION_CHOICES, null=False, blank=False
#     )
#     users_django_id = OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE
#         )
#     roles_djange_id = OneToOneField(
#         settings.AUTH_GROUPS_MODEL, on_delete=models.CASCADE
#         )


# class Seating_Plan(models.Model):
#     pass


# class Seating_Position(models.Model):
#     pass


# class Session(models.Model):
#     pass
