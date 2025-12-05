from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # you can tighten later

from .models import (
    Country,
    Language,
    SeriesType,
    ProductionHouse,
    Producer,
    ProducerHouse,
    WebSeries,
    WebSeriesType,
    Episode,
    WebSeriesDubbing,
    WebSeriesSubtitle,
    WebSeriesCountry,
    Contract,
    ViewerAccount,
    Subscription,
    Feedback,
    Schedule,
)

from .serializers import (
    CountrySerializer,
    LanguageSerializer,
    SeriesTypeSerializer,
    ProductionHouseSerializer,
    ProducerSerializer,
    ProducerHouseSerializer,
    WebSeriesSerializer,
    WebSeriesTypeSerializer,
    EpisodeSerializer,
    WebSeriesDubbingSerializer,
    WebSeriesSubtitleSerializer,
    WebSeriesCountrySerializer,
    ContractSerializer,
    ViewerAccountSerializer,
    SubscriptionSerializer,
    FeedbackSerializer,
    ScheduleSerializer,
)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]


class CountryViewSet(BaseViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class LanguageViewSet(BaseViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SeriesTypeViewSet(BaseViewSet):
    queryset = SeriesType.objects.all()
    serializer_class = SeriesTypeSerializer


class ProductionHouseViewSet(BaseViewSet):
    queryset = ProductionHouse.objects.all()
    serializer_class = ProductionHouseSerializer


class ProducerViewSet(BaseViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerHouseViewSet(BaseViewSet):
    queryset = ProducerHouse.objects.all()
    serializer_class = ProducerHouseSerializer


class WebSeriesViewSet(BaseViewSet):
    queryset = WebSeries.objects.all()
    serializer_class = WebSeriesSerializer


class WebSeriesTypeViewSet(BaseViewSet):
    queryset = WebSeriesType.objects.all()
    serializer_class = WebSeriesTypeSerializer


class EpisodeViewSet(BaseViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class WebSeriesDubbingViewSet(BaseViewSet):
    queryset = WebSeriesDubbing.objects.all()
    serializer_class = WebSeriesDubbingSerializer


class WebSeriesSubtitleViewSet(BaseViewSet):
    queryset = WebSeriesSubtitle.objects.all()
    serializer_class = WebSeriesSubtitleSerializer


class WebSeriesCountryViewSet(BaseViewSet):
    queryset = WebSeriesCountry.objects.all()
    serializer_class = WebSeriesCountrySerializer


class ContractViewSet(BaseViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ViewerAccountViewSet(BaseViewSet):
    queryset = ViewerAccount.objects.all()
    serializer_class = ViewerAccountSerializer


class SubscriptionViewSet(BaseViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class FeedbackViewSet(BaseViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
