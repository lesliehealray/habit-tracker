from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class CustomUser(AbstractUser):
    profile_name = models.CharField(max_length=30, blank=True)
    profile_description = models.TextField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

class Habit(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user'
    )
    title = models.CharField(max_length=50)
    slug =  models.SlugField(blank=True)
    created_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    habit_achieved = models.BooleanField(default=False)
    total_success_number = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        blank=True
        )
    supporters = models.ManyToManyField(
        to='Supporter',
        blank=True,
        related_name='supporter'
    )

    def __str__(self):
        return self.title 

class Log(models.Model):
    log_number_completed = models.DecimalField(
        max_digits=9, 
        decimal_places=2
    )
    log_detail = models.CharField(max_length=255)
    habit = models.ForeignKey(
        to=Habit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='habit_log'
    )

    def __str__(self):
        return self.log_detail

class Comment(models.Model):
    log = models.ForeignKey(
        to=Log,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='log'
    )
    comment_body = models.CharField(max_length=255)

    def __str__(self):
        return self.comment_body


class Supporter(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
    )
    accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=64)
    


    