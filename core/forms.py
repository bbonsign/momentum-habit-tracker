from django import forms

from .models import Habit, Log, Observer


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('title', 'action', 'goal', 'units',)


class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('habit', 'date', 'achievement',)
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'}),
        }


class ObserverForm(forms.ModelForm):

    class Meta:
        model = Observer
        fields = ('observer',)
        widgets = {
            'observer': forms.TextInput()
        }
        help_texts = {
            'observer': "Username of the person you'd like to add as an observer to this habit (case-sensitive)",
        }