from core.models import (
    Country, Language, SeriesType, ProductionHouse, Producer, ProducerHouse,
    WebSeries, WebSeriesType, Episode, WebSeriesDubbing, WebSeriesSubtitle,
    WebSeriesCountry, Contract, ViewerAccount, Subscription, Feedback, Schedule
)
from django.utils import timezone
from datetime import date, datetime


def run():
    # ---------------------------------------
    # 1. Countries
    # ---------------------------------------
    countries = [
        Country(country_code="US", country_name="United States"),
        Country(country_code="IN", country_name="India"),
        Country(country_code="UK", country_name="United Kingdom"),
    ]
    Country.objects.bulk_create(countries, ignore_conflicts=True)

    # ---------------------------------------
    # 2. Languages
    # ---------------------------------------
    languages = [
        Language(language_code="EN", country_name="English"),
        Language(language_code="HI", country_name="Hindi"),
        Language(language_code="ES", country_name="Spanish"),
    ]
    Language.objects.bulk_create(languages, ignore_conflicts=True)

    # ---------------------------------------
    # 3. Series Types
    # ---------------------------------------
    types = [
        SeriesType(series_type_id="ST1", type_name="Drama"),
        SeriesType(series_type_id="ST2", type_name="Thriller"),
    ]
    SeriesType.objects.bulk_create(types, ignore_conflicts=True)

    # ---------------------------------------
    # 4. Production House
    # ---------------------------------------
    ph1 = ProductionHouse.objects.create(
        production_house_id="PH1",
        prod_house_name="Sunshine Studios",
        street="123 Main St",
        city="Los Angeles",
        state="CA",
        country=Country.objects.get(country_code="US"),
        zipcode="90001",
        year_established=1995,
    )

    # ---------------------------------------
    # 5. Producer
    # ---------------------------------------
    pr1 = Producer.objects.create(
        producer_id="PR1",
        producer_name="John Carter",
        email_id="john@example.com",
        phone_number="1234567890",
        city="Los Angeles",
        state="CA",
        country=Country.objects.get(country_code="US"),
        zipcode="90001",
    )

    # ---------------------------------------
    # 6. Producer ↔ Production House
    # ---------------------------------------
    ProducerHouse.objects.get_or_create(producer=pr1, production_house=ph1)

    # ---------------------------------------
    # 7. Web Series
    # ---------------------------------------
    ws1 = WebSeries.objects.create(
        web_series_id="WS1",
        name="Edge of Tomorrow",
        no_of_episodes=3,
        original_language=Language.objects.get(language_code="EN"),
        release_date=date(2024, 1, 1),
        description="Sci-fi thriller series",
        producer_house=ph1,
        producer=pr1,
    )

    # ---------------------------------------
    # 8. WebSeriesType
    # ---------------------------------------
    WebSeriesType.objects.get_or_create(
        web_series=ws1, series_type=SeriesType.objects.get(series_type_id="ST2")
    )

    # ---------------------------------------
    # 9. Episodes (3 episodes)
    # ---------------------------------------
    episodes = [
        Episode(
            episode_id="E1",
            web_series=ws1,
            episode_number=1,
            episode_title="Beginning",
            total_viewers=5000,
            tech_interruption_flag="N",
            duration_minutes=45,
        ),
        Episode(
            episode_id="E2",
            web_series=ws1,
            episode_number=2,
            episode_title="Mid War",
            total_viewers=6000,
            tech_interruption_flag="N",
            duration_minutes=50,
        ),
        Episode(
            episode_id="E3",
            web_series=ws1,
            episode_number=3,
            episode_title="Final Stand",
            total_viewers=8000,
            tech_interruption_flag="N",
            duration_minutes=55,
        ),
    ]
    Episode.objects.bulk_create(episodes, ignore_conflicts=True)

    # ---------------------------------------
    # 10. Dubbing
    # ---------------------------------------
    WebSeriesDubbing.objects.get_or_create(
        web_series=ws1,
        language=Language.objects.get(language_code="HI"),
        defaults={
            "dubbing_studio": "SoundLab India",
            "dubbing_artist": "Amit Sharma",
            "audio_quality": "Dolby",
            "release_date": date(2024, 2, 15),
        },
    )

    # ---------------------------------------
    # 11. Subtitles
    # ---------------------------------------
    WebSeriesSubtitle.objects.get_or_create(
        web_series=ws1, language=Language.objects.get(language_code="ES")
    )

    # ---------------------------------------
    # 12. Country Availability
    # ---------------------------------------
    for cc in ["US", "IN", "UK"]:
        WebSeriesCountry.objects.get_or_create(
            web_series=ws1, country=Country.objects.get(country_code=cc)
        )

    # ---------------------------------------
    # 13. Contract
    # ---------------------------------------
    Contract.objects.get_or_create(
        contract_id="C1",
        web_series=ws1,
        prod_house=ph1,
        contract_start_date=date(2023, 12, 1),
        contract_end_date=date(2025, 12, 1),
        per_episode_charge=20000,
        total_contract_value=60000,
        contract_status="Active",
    )

    # ---------------------------------------
    # 14. Viewer Accounts
    # ---------------------------------------
    viewers = [
        ViewerAccount(
            account_id="A1",
            name="Alice Johnson",
            city="New York",
            state="NY",
            country=Country.objects.get(country_code="US"),
            email="alice@example.com",
            phone_number="1111111111",
            payment_method="Card",
            monthly_charge=9.99,
        ),
        ViewerAccount(
            account_id="A2",
            name="Rahul Verma",
            city="Mumbai",
            state="MH",
            country=Country.objects.get(country_code="IN"),
            email="rahul@example.com",
            phone_number="2222222222",
            payment_method="UPI",
            monthly_charge=4.99,
        ),
    ]
    ViewerAccount.objects.bulk_create(viewers, ignore_conflicts=True)

    # ---------------------------------------
    # 15. Subscriptions
    # ---------------------------------------
    Subscription.objects.get_or_create(
        subscription_id="S1",
        account=ViewerAccount.objects.get(account_id="A1"),
        plan_type="Premium",
        start_date=date(2024, 1, 1),
    )
    Subscription.objects.get_or_create(
        subscription_id="S2",
        account=ViewerAccount.objects.get(account_id="A2"),
        plan_type="Basic",
        start_date=date(2024, 1, 5),
    )

    # ---------------------------------------
    # 16. Feedback
    # ---------------------------------------
    Feedback.objects.get_or_create(
        account=ViewerAccount.objects.get(account_id="A1"),
        web_series=ws1,
        feedback_text="Amazing series!",
        rating=5,
        feedback_date=date(2024, 2, 1),
    )

    Feedback.objects.get_or_create(
        account=ViewerAccount.objects.get(account_id="A2"),
        web_series=ws1,
        feedback_text="Good but slow in parts.",
        rating=4,
        feedback_date=date(2024, 2, 3),
    )

    # ---------------------------------------
    # 17. Schedule (Episode-country)
    # ---------------------------------------
    schedules = [
        Schedule(
            schedule_id="SCH1",
            episode=Episode.objects.get(episode_id="E1"),
            country=Country.objects.get(country_code="US"),
            schedule_start_ts=datetime(2024, 3, 1, 18, 0),
            schedule_end_ts=datetime(2024, 3, 1, 19, 0),
            is_live_flag="Y",
        ),
        Schedule(
            schedule_id="SCH2",
            episode=Episode.objects.get(episode_id="E2"),
            country=Country.objects.get(country_code="IN"),
            schedule_start_ts=datetime(2024, 3, 2, 18, 0),
            schedule_end_ts=datetime(2024, 3, 2, 19, 0),
            is_live_flag="N",
        ),
        Schedule(
            schedule_id="SCH3",
            episode=Episode.objects.get(episode_id="E3"),
            country=Country.objects.get(country_code="UK"),
            schedule_start_ts=datetime(2024, 3, 3, 18, 0),
            schedule_end_ts=datetime(2024, 3, 3, 19, 0),
            is_live_flag="N",
        ),
    ]
    Schedule.objects.bulk_create(schedules, ignore_conflicts=True)

    print("🎉 Bulk insert completed successfully!")


# Run in Django shell:
# >>> from path.to.this.file import run
# >>> run()