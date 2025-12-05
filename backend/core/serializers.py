from rest_framework import serializers
from .models import (
    User,
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SeriesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesType
        fields = "__all__"


class ProductionHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionHouse
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class ProducerHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerHouse
        fields = "__all__"


class WebSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeries
        fields = "__all__"


class WebSeriesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeriesType
        fields = "__all__"


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"


class WebSeriesDubbingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeriesDubbing
        fields = "__all__"


class WebSeriesSubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeriesSubtitle
        fields = "__all__"


class WebSeriesCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSeriesCountry
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class ViewerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerAccount
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
