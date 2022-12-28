from .models import Seating_Position, Seating_Plan, Player_Project
from django import forms


class SeatingPositionForm(forms.ModelForm):
    class Meta:
        model = Seating_Position
        fields = ('player',
                  'position_number',
                  )


class EditSeatingPlan(forms.ModelForm):
    class Meta:
        model = Seating_Position
        fields = ('position_number',)


class SeatingPlanForm(forms.ModelForm):
    class Meta:
        model = Seating_Plan
        fields = ('plan_status',)


class PlayerProjectFormPL(forms.ModelForm):

    class Meta:
        model = Player_Project
        fields = ('off_reduced_rep',)
