from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebSeriesViewSet, EpisodeViewSet, ScheduleViewSet, WebSeriesDubbingViewSet

router = DefaultRouter()
router.register('series', WebSeriesViewSet)
router.register('episodes', EpisodeViewSet)
router.register('schedule', ScheduleViewSet)
router.register('dubbing', WebSeriesDubbingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
