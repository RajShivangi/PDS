from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsEmployee
from .models import WebSeries, Episode, Schedule, WebSeriesDubbing
from .serializers import WebSeriesSerializer, EpisodeSerializer, ScheduleSerializer, WebSeriesDubbingSerializer
from rest_framework.permissions import IsAuthenticated

class WebSeriesViewSet(viewsets.ModelViewSet):
    queryset = WebSeries.objects.all()
    serializer_class = WebSeriesSerializer
    def get_permissions(self):
        if self.action == 'destroy':
            return [IsEmployee()]
        return []
        # return [IsAuthenticated()]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []


class WebSeriesDubbingViewSet(viewsets.ModelViewSet):
    queryset = WebSeriesDubbing.objects.all()
    serializer_class = WebSeriesDubbingSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []

