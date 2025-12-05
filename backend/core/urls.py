from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CountryViewSet,
    LanguageViewSet,
    SeriesTypeViewSet,
    ProductionHouseViewSet,
    ProducerViewSet,
    ProducerHouseViewSet,
    WebSeriesViewSet,
    WebSeriesTypeViewSet,
    EpisodeViewSet,
    WebSeriesDubbingViewSet,
    WebSeriesSubtitleViewSet,
    WebSeriesCountryViewSet,
    ContractViewSet,
    ViewerAccountViewSet,
    SubscriptionViewSet,
    FeedbackViewSet,
    ScheduleViewSet,
)

router = DefaultRouter()
router.register("countries", CountryViewSet)
router.register("languages", LanguageViewSet)
router.register("series-types", SeriesTypeViewSet)
router.register("production-houses", ProductionHouseViewSet)
router.register("producers", ProducerViewSet)
router.register("producer-houses", ProducerHouseViewSet)
router.register("series", WebSeriesViewSet)
router.register("series-types-map", WebSeriesTypeViewSet)
router.register("episodes", EpisodeViewSet)
router.register("dubbing", WebSeriesDubbingViewSet)
router.register("subtitles", WebSeriesSubtitleViewSet)
router.register("series-country", WebSeriesCountryViewSet)
router.register("contracts", ContractViewSet)
router.register("viewers", ViewerAccountViewSet)
router.register("subscriptions", SubscriptionViewSet)
router.register("feedback", FeedbackViewSet)
router.register("schedules", ScheduleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
