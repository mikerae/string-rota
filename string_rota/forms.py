# pylint: disable=no-member
""" Forms for string-rota """
from django import forms
from django.core.exceptions import ValidationError
from .models import (
    SeatingPosition,
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


class EditSeatingPositionForm(forms.ModelForm):
    """Form to edit Seating Position"""

    class Meta:
        """Customisation for SeatingPositionForm"""

        model = SeatingPosition
        fields = [
            "position_number",
        ]

    def __init__(self, section, seating_plan, *args, **kwargs):
        """
        Populate player field with instance.player to be edited
        Provide access to current section and seating plan
        """
        super().__init__(*args, **kwargs)

        self.player = self.instance.player
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
        if not position_number == self.instance.position_number:
            if position_number in allocated_positions_list:
                raise ValidationError(
                    (
                        f" Seating Position {position_number} has already \
                            been allocated. Please choose another position."
                    ),
                    code="NA",
                )
        print("position is unchanged")
        return position_number


class PlayerProjectForm(forms.ModelForm):
    """Form to create a PlayerProject record"""

    class Meta:
        """Customisation for PlayerProject form"""

        model = PlayerProject
        fields = ("off_reduced_rep",)


class ReserveForm(forms.ModelForm):
    """Form to allocate Reserve  player to a project"""

    class Meta:
        """Customisation for Reduced form"""

        model = PlayerProject
        fields = ("player",)

    def __init__(self, section, seating_plan, *args, **kwargs):
        """
        Populate player field with section members not playing in project.
        """
        super().__init__(*args, **kwargs)
        players = Player.objects.filter(section=section)
        allocated_players = seating_plan.players.all()
        not_playing_players = players.exclude(pk__in=allocated_players)

        self.fields["player"].queryset = not_playing_players
