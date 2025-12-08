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
    # Input: Accepts text string (e.g., "English", "wer")
    language = serializers.CharField(write_only=True)
    
    # Output: Shows the full language object in API responses (optional but good for frontend)
    language_details = LanguageSerializer(source='language', read_only=True)

    class Meta:
        model = WebSeries
        fields = [
            "web_series_id", 
            "name", 
            "no_of_episodes", 
            "release_date", 
            "description", 
            "language",          # Input (Write)
            "language_details",  # Output (Read)
            "producer",
            "producer_house",
            "image_url"
        ]

    def create(self, validated_data):
        # 1. Remove the string 'language' from the data so it doesn't crash the model
        language_name = validated_data.pop('language')
        
        # 2. Generate a code (First 10 chars, uppercase)
        # e.g., "French" -> "FRENCH", "LongLanguageName" -> "LONGLANGUA"
        lang_code = language_name[:10].upper()
        
        # 3. Get existing Language OR Create a new one
        language_instance, created = Language.objects.get_or_create(
            country_name=language_name,
            defaults={'language_code': lang_code}
        )
        
        # 4. Create the WebSeries using the actual Language INSTANCE
        web_series = WebSeries.objects.create(
            language=language_instance,  # <--- Assign the Object, not the string
            **validated_data
        )
        return web_series

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
