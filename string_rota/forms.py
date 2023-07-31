""" Forms for string-rota """
from django import forms
from .models import SeatingPosition, SeatingPlan, PlayerProject


class SeatingPositionForm(forms.ModelForm):
    """ Form to edit Seating Position  """
    class Meta:
        """ Customisation for SeatingPositionForm """
        model = SeatingPosition
        fields = ('player',
                  'position_number',
                  )


class EditSeatingPlan(forms.ModelForm):
    """ Form to edit Seating Plan """
    class Meta:
        """ Customisation for EditSeatingplan form """
        model = SeatingPosition
        fields = ('position_number',)


class SeatingPlanForm(forms.ModelForm):
    """ Form to Create a Seating Plan """
    class Meta:
        """ Customisation for SeatingPlan form """
        model = SeatingPlan
        fields = ('plan_status',)


class PlayerProjectForm(forms.ModelForm):
    """ Form to create a PlayerProject record """

    class Meta:
        """ Customisation for PlayerProject form """
        model = PlayerProject
        fields = ('off_reduced_rep',)


class EditPlayerProjectForm(forms.ModelForm):
    """ Form to edit a PlayerProject record """

    class Meta:
        """ Customisation for  EditPlayerProjectForm"""
        model = PlayerProject
        fields = ('performance_status',)


class ReserveReducedForm(forms.ModelForm):
    """ Form to manage Reserve and Reduced status of a player for a project """

    class Meta:
        """ Customisation for ReserveReduced form """
        model = PlayerProject
        fields = ('performance_status',
                  'off_reduced_rep',
                  )
