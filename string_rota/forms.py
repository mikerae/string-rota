from .models import Seating_Position, Seating_Plan, Player_Project
from django import forms


class SeatingPositionForm(forms.ModelForm):
    class Meta:
        model = Seating_Position
        fields = ('position_number',
                  'player',
                  )


class SeatingPlanForm(forms.ModelForm):
    class Meta:
        model = Seating_Plan
        fields = ('plan_status',)


class PlayerProjectForm(forms.ModelForm):
    class Meta:
        model = Player_Project
        fields = ('performance_status',
                  'off_reduced_rep',
                  )


class RotaForm(SeatingPlanForm, SeatingPositionForm, PlayerProjectForm)
