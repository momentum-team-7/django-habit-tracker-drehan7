from django import forms
from .models import Profile, HabitLog, Habit, User

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name']


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title','description', 'goal']