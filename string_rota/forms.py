# pylint: disable=no-member
""" Forms for string-rota """
from django import forms
from django.core.exceptions import ValidationError
from .models import (
    SeatingPosition,
    SeatingPlan,
    PlayerProject,
    Player,
)  # noqa E501


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
        """
        Populate player field with current section players
        Provide access to current section and seating plan
        """
        super().__init__(*args, **kwargs)
        players = Player.objects.filter(section=section)
        allocated_players = seating_plan.players.all()
        available_players = players.exclude(pk__in=allocated_players)
        self.fields["player"].queryset = available_players
        self.section = section
        self.seating_plan = seating_plan

    def clean_position_number(self):
        """
        Validator for seating position number.
        'strength' sets the upper position limit,

        """

        strength = self.section.default_strength
        plan_custom_strength = self.seating_plan.custom_strength
        allocated_positions = SeatingPosition.objects.filter(
            seating_plan=self.seating_plan
        ).all()  # noqa E501
        allocated_positions_list = []
        position_number = self.cleaned_data["position_number"]
        for position in allocated_positions:
            allocated_positions_list.append(position.position_number)
        if plan_custom_strength:
            strength = plan_custom_strength

        if position_number < 1 or position_number > strength:
            raise ValidationError(
                (
                    f"This project has {strength} \
                        seating positions. Please choose an approriate \
                            seating position."
                ),
                code="range",
            )

        if position_number in allocated_positions_list:
            raise ValidationError(
                (
                    f" Seating Position {position_number} has already \
                        been allocated. Please choose another position."
                ),
                code="NA",
            )
        return position_number


class EditSeatingPlanForm(forms.ModelForm):
    """Form to edit Seating Plan"""

    class Meta:
        """Customisation for EditSeatingplan form"""

        model = SeatingPosition
        fields = ("position_number",)

    def __init__(self, section, seating_plan, instance, *args, **kwargs):
        """Provide access to current section and seating plan"""
        super().__init__(*args, **kwargs)
        self.section = section
        self.seating_plan = seating_plan

    def clean_position_number(self):
        """
        Validator for seating position number.
        'strength' sets the upper position limit,

        """
        strength = self.section.default_strength
        plan_custom_strength = self.seating_plan.custom_strength
        allocated_positions = SeatingPosition.objects.filter(
            seating_plan=self.seating_plan
        ).all()  # noqa E501
        allocated_positions_list = []
        position_number = self.cleaned_data["position_number"]
        for position in allocated_positions:
            allocated_positions_list.append(position.position_number)
        if plan_custom_strength:
            strength = plan_custom_strength

        if position_number < 1 or position_number > strength:
            raise ValidationError(
                (
                    f"This project has {strength} \
                        seating positions. Please choose an approriate \
                            seating position."
                ),
                code="range",
            )

        if position_number in allocated_positions_list:
            raise ValidationError(
                (
                    f" Seating Position {position_number} has already \
                        been allocated. Please choose another position."
                ),
                code="NA",
            )
        return position_number


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
