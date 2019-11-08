from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import DateField
from django.contrib.admin.widgets import AdminDateWidget
from tracker.models import CustomUser, Habit

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'start_date', 'number_per_day', 'total_number']