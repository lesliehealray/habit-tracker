from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tracker.models import CustomUser, Habit

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_name', 'profile_description', 'avatar')
