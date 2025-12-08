from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    User, Country, Language, SeriesType, ProductionHouse, Producer, ProducerHouse,
    WebSeries, WebSeriesType, Episode, WebSeriesDubbing, WebSeriesSubtitle,
    WebSeriesCountry, Contract, ViewerAccount, Subscription, Feedback, Schedule
)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role  # Embed role in token
        token['username'] = user.username
        return token

# 2. User Registration Serializer (For Admin to add Customers)
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']

    def create(self, validated_data):
        # This securely hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            role=validated_data.get('role', 'customer')
        )
        return user

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
    language = serializers.SlugRelatedField(
        slug_field="country_name",         
        queryset=Language.objects.all()   
    )

    class Meta:
        model = WebSeries
        fields = "__all__"
    
        def validate_language(self, value):
        # If the value is already a Language instance, return it
            if isinstance(value, Language):
                return value

            # Try to match by primary key (language_code)
            try:
                return Language.objects.get(pk=value)
            except Language.DoesNotExist:
                pass

            # Try to match by the country_name string
            try:
                return Language.objects.get(country_name__iexact=value)
            except Language.DoesNotExist:
                raise serializers.ValidationError(
                    f"Language '{value}' does not exist."
                )


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
