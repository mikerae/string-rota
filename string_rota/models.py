from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200, null=False, blank=False)


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


# class Project_Repertoire(models.Model):
#     pass


# class Repertoire(model.Models):
#     def vln1_nos(self.intrumentation):
#         pass

#     def vln2_nos(self.intrumentation):
#         pass

#     def vla_nos(self.intrumentation):
#         pass

#     def vlc_nos(self.intrumentation):
#         pass

#     def db_nos(self.intrumentation):
#         pass

#     name = models.CharField(max_length=200, unique=True)
#     intrumentation = models.CharField(max_length=14)
#     vln1_nos = vln1_nos
#     vln2_nos = vln2_nos
#     vla_nos = vla_nos
#     vlc_nos = vlc_nos
#     db_nos = db_nos
