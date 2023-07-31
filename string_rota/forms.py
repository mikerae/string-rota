# pylint: disable=no-member
""" Forms for string-rota """
from django import forms
from .models import SeatingPosition, SeatingPlan, PlayerProject, Player


class SeatingPositionForm(forms.ModelForm):
    """Form to edit Seating Position"""

    class Meta:
        """Customisation for SeatingPositionForm"""

        model = SeatingPosition
        fields = [
            "player",
            "position_number",
        ]

    def __init__(self, section, seating_plan, *args, **kwargs):
        """Populate player field with current section players"""
        super().__init__(*args, **kwargs)
        players = Player.objects.filter(section=section)
        allocated_players = seating_plan.players.all()
        available_players = players.exclude(pk__in=allocated_players)
        print(f"available_players: {available_players}")
        self.fields["player"].queryset = available_players


class EditSeatingPlanForm(forms.ModelForm):
    """Form to edit Seating Plan"""

    class Meta:
        """Customisation for EditSeatingplan form"""

        model = SeatingPosition
        fields = ("position_number",)


class SeatingPlanForm(forms.ModelForm):
    """Form to Create a Seating Plan"""

    class Meta:
        """Customisation for SeatingPlan form"""

        model = SeatingPlan
        fields = ("plan_status",)


class PlayerProjectForm(forms.ModelForm):
    """Form to create a PlayerProject record"""

    class Meta:
        """Customisation for PlayerProject form"""

        model = PlayerProject
        fields = ("off_reduced_rep",)


class EditPlayerProjectForm(forms.ModelForm):
    """Form to edit a PlayerProject record"""

    class Meta:
        """Customisation for  EditPlayerProjectForm"""

        model = PlayerProject
        fields = ("performance_status",)


class ReserveReducedForm(forms.ModelForm):
    """Form to manage Reserve and Reduced status of a player for a project"""

    class Meta:
        """Customisation for ReserveReduced form"""

        model = PlayerProject
        fields = (
            "performance_status",
            "off_reduced_rep",
        )
