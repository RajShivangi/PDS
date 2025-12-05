# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("employee", "Employee"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")

    # encrypted password automatically handled by Django

class Country(models.Model):
    country_code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.country_name

class Language(models.Model):
    language_code = models.CharField(max_length=10, primary_key=True)
    country_name = models.CharField(max_length=50, unique=True)

class WebSeries(models.Model):
    web_series_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    no_of_episodes = models.IntegerField()
    language = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=200, null=True)

class Episode(models.Model):
    episode_id = models.CharField(max_length=20, primary_key=True)
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    episode_title = models.CharField(max_length=150)
    schedule_start_ts = models.DateField()
    schedule_end_ts = models.DateField()
    total_viewers = models.IntegerField()
    tech_interruption_flag = models.CharField(max_length=1)
    duration_minutes = models.IntegerField()

class WebSeriesDubbing(models.Model):
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    dubbing_studio = models.CharField(max_length=120, null=True)
    dubbing_artist = models.CharField(max_length=120, null=True)
    audio_quality = models.CharField(max_length=20, null=True)
    release_date = models.DateField(null=True)

    class Meta:
        unique_together = ('web_series', 'language')

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    schedule_start_ts = models.DateField()
    schedule_end_ts = models.DateField()
    is_live_flag = models.CharField(max_length=1, default='N')

