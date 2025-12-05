from rest_framework import serializers
from .models import WebSeries, Episode, Schedule, WebSeriesDubbing

class WebSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeries
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class WebSeriesDubbingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeriesDubbing
        fields = '__all__'
