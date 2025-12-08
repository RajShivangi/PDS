# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# -------------------------
# Custom User (for auth/roles)
# -------------------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("employee", "Employee"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")

    # encrypted password automatically handled by Django

# -------------------------
# Reference / Lookup Tables
# -------------------------
class Country(models.Model):
    country_code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.country_name

class Language(models.Model):
    language_code = models.CharField(max_length=10, primary_key=True)
    country_name = models.CharField(max_length=50, unique=True)

class SeriesType(models.Model):
    # SSD_SERIES_TYPE
    series_type_id = models.CharField(max_length=20, primary_key=True)
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type_name


# -------------------------
# Producer / Production Side
# -------------------------

class ProductionHouse(models.Model):
    # SSD_PRODUCTION_HOUSE
    production_house_id = models.CharField(max_length=20, primary_key=True)
    prod_house_name = models.CharField(max_length=100, unique=True)
    street = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    year_established = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.prod_house_name


class Producer(models.Model):
    # SSD_PRODUCER
    producer_id = models.CharField(max_length=20, primary_key=True)
    producer_name = models.CharField(max_length=120)
    email_id = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    street_address = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.producer_name


class ProducerHouse(models.Model):
    # SSD_PRODUCER_HOUSE (bridge between Producer and ProductionHouse)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("producer", "production_house")

    def __str__(self):
        return f"{self.producer} @ {self.production_house}"


# -------------------------
# Web Series and Related
# -------------------------
class WebSeries(models.Model):
    # SSD_WEB_SERIES
    web_series_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    no_of_episodes = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    description = models.CharField(max_length=500, blank=True, null=True)
    producer_house = models.ForeignKey(
        ProductionHouse, on_delete=models.SET_NULL, null=True, blank=True
    )
    producer = models.ForeignKey(
        Producer, on_delete=models.SET_NULL, null=True, blank=True
    )

    image_url = models.URLField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.name


class WebSeriesType(models.Model):
    # SSD_WEB_SERIES_TYPE (bridge between web_series and series_type)
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    series_type = models.ForeignKey(SeriesType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("web_series", "series_type")

    def __str__(self):
        return f"{self.web_series} - {self.series_type}"


class Episode(models.Model):
    # SSD_EPISODE
    episode_id = models.CharField(max_length=20, primary_key=True)
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    episode_title = models.CharField(max_length=200)
    schedule_start_ts = models.DateTimeField(blank=True, null=True)
    schedule_end_ts = models.DateTimeField(blank=True, null=True)
    total_viewers = models.IntegerField(default=0)
    tech_interruption_flag = models.CharField(
        max_length=1, choices=(("Y", "Yes"), ("N", "No")), default="N"
    )
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"{self.web_series.name} - Ep {self.episode_number}"



# -------------------------
# Dubbing and Subtitles
# -------------------------
class WebSeriesDubbing(models.Model):
    # Added table
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    dubbing_studio = models.CharField(max_length=120, blank=True, null=True)
    dubbing_artist = models.CharField(max_length=120, blank=True, null=True)
    audio_quality = models.CharField(max_length=20, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ("web_series", "language")

    def __str__(self):
        return f"{self.web_series} - Dubbed in {self.language}"


class WebSeriesSubtitle(models.Model):
    # SSD_WEB_SERIES_SUBTITLE
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("web_series", "language")

    def __str__(self):
        return f"{self.web_series} - Subtitles: {self.language}"


# -------------------------
# Country Availability (bridge)
# -------------------------
class WebSeriesCountry(models.Model):
    # SR_WEB_SERIES_COUNTRY_FK
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("web_series", "country")

    def __str__(self):
        return f"{self.web_series} in {self.country}"


# -------------------------
# Contract
# -------------------------
class Contract(models.Model):
    # SSD_CONTRACT
    contract_id = models.CharField(max_length=20, primary_key=True)
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    prod_house = models.ForeignKey(
        ProductionHouse, on_delete=models.SET_NULL, null=True, blank=True
    )
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    per_episode_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total_contract_value = models.DecimalField(max_digits=12, decimal_places=2)
    contract_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Contract {self.contract_id} - {self.web_series}"


# -------------------------
# Viewer / Subscription / Feedback
# -------------------------
class ViewerAccount(models.Model):
    # SSD_VIEWER_ACCOUNT
    account_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=40, blank=True, null=True)
    monthly_charge = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.account_id} - {self.name}"


class Subscription(models.Model):
    # SSD_SUBSCRIPTION
    subscription_id = models.CharField(max_length=20, primary_key=True)
    account = models.ForeignKey(ViewerAccount, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.subscription_id} ({self.plan_type})"


class Feedback(models.Model):
    # SSD_FEEDBACK
    account = models.ForeignKey(ViewerAccount, on_delete=models.CASCADE)
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    feedback_text = models.CharField(max_length=2000, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    feedback_date = models.DateField()

    def __str__(self):
        return f"{self.account} on {self.web_series}"


# -------------------------
# Schedule (episode-level per country)
# -------------------------
class Schedule(models.Model):
    # New SCHEDULE table
    schedule_id = models.CharField(max_length=20, primary_key=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    schedule_start_ts = models.DateTimeField()
    schedule_end_ts = models.DateTimeField()
    is_live_flag = models.CharField(
        max_length=1, choices=(("Y", "Yes"), ("N", "No")), default="N"
    )

    def __str__(self):
        return f"{self.episode} in {self.country}"

