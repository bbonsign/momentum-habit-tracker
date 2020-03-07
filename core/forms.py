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
        # widgets = {
        #     # 'observer': forms.TextInput(queryset=Users.objects.all) attrs={'required': ''})
        # }
