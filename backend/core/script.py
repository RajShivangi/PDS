from core.models import (
    Country, Language, SeriesType, ProductionHouse, Producer, ProducerHouse,
    WebSeries, WebSeriesType, Episode, WebSeriesDubbing, WebSeriesSubtitle,
    WebSeriesCountry, Contract, ViewerAccount, Subscription, Feedback, Schedule
)
from datetime import date, datetime


def run():

    # -------------------------------
    # 1. Countries
    # -------------------------------
    Country.objects.bulk_create([
        Country(country_code="US", country_name="United States"),
        Country(country_code="IN", country_name="India"),
        Country(country_code="JP", country_name="Japan"),
        Country(country_code="BR", country_name="Brazil"),
    ], ignore_conflicts=True)

    # -------------------------------
    # 2. Languages
    # -------------------------------
    Language.objects.bulk_create([
        Language(language_code="EN", country_name="English"),
        Language(language_code="HI", country_name="Hindi"),
        Language(language_code="JP_L", country_name="Japanese"),
        Language(language_code="PT", country_name="Portuguese"),
    ], ignore_conflicts=True)

    # -------------------------------
    # 3. Series Types
    # -------------------------------
    SeriesType.objects.bulk_create([
        SeriesType(series_type_id="T1", type_name="Mystery"),
        SeriesType(series_type_id="T2", type_name="Action"),
        SeriesType(series_type_id="T3", type_name="Comedy"),
        SeriesType(series_type_id="T4", type_name="Sci-Fi"),
    ], ignore_conflicts=True)

    # -------------------------------
    # Production Houses
    # -------------------------------
    ph1 = ProductionHouse.objects.create(
        production_house_id="PH10",
        prod_house_name="Blue Horizon Studios",
        street="12 Maple Rd",
        city="Seattle",
        state="WA",
        country=Country.objects.get(country_code="US"),
        zipcode="98101",
        year_established=2001
    )

    ph2 = ProductionHouse.objects.create(
        production_house_id="PH11",
        prod_house_name="Kitsune Media",
        street="77 Sakura Lane",
        city="Tokyo",
        state="Tokyo",
        country=Country.objects.get(country_code="JP"),
        zipcode="10001",
        year_established=1992
    )

    ph3 = ProductionHouse.objects.create(
        production_house_id="PH12",
        prod_house_name="Rio Cinematics",
        street="88 Copacabana St",
        city="Rio",
        state="RJ",
        country=Country.objects.get(country_code="BR"),
        zipcode="22070",
        year_established=1999
    )

    # -------------------------------
    # Producers
    # -------------------------------
    pr1 = Producer.objects.create(
        producer_id="P10",
        producer_name="Elena Morris",
        city="Seattle",
        state="WA",
        country=Country.objects.get(country_code="US")
    )

    pr2 = Producer.objects.create(
        producer_id="P11",
        producer_name="Hiro Tanaka",
        city="Tokyo",
        state="Tokyo",
        country=Country.objects.get(country_code="JP")
    )

    pr3 = Producer.objects.create(
        producer_id="P12",
        producer_name="Carlos Mendes",
        city="Rio",
        state="RJ",
        country=Country.objects.get(country_code="BR")
    )

    ProducerHouse.objects.get_or_create(producer=pr1, production_house=ph1)
    ProducerHouse.objects.get_or_create(producer=pr2, production_house=ph2)
    ProducerHouse.objects.get_or_create(producer=pr3, production_house=ph3)

    # ---------------------------------------------------------
    # WEB SERIES 1 — “Shadows of Yesterday” (Mystery)
    # ---------------------------------------------------------
    ws1 = WebSeries.objects.create(
        web_series_id="WS10",
        name="Shadows of Yesterday",
        no_of_episodes=3,
        language=Language.objects.get(language_code="EN"),
        release_date=date(2024, 2, 1),
        description="A detective unravels a decades-old cold case.",
        producer_house=ph1,
        producer=pr1
    )

    WebSeriesType.objects.create(web_series=ws1, series_type=SeriesType.objects.get(series_type_id="T1"))

    Episode.objects.bulk_create([
        Episode(episode_id="E10", web_series=ws1, episode_number=1, episode_title="The Letter", total_viewers=5200, tech_interruption_flag="N", duration_minutes=50),
        Episode(episode_id="E11", web_series=ws1, episode_number=2, episode_title="Lost Evidence", total_viewers=5800, tech_interruption_flag="N", duration_minutes=48),
        Episode(episode_id="E12", web_series=ws1, episode_number=3, episode_title="Truth Uncovered", total_viewers=6400, tech_interruption_flag="N", duration_minutes=55),
    ])

    WebSeriesDubbing.objects.create(web_series=ws1, language=Language.objects.get(language_code="HI"), dubbing_studio="Delhi Dubs", dubbing_artist="Arjun Mehra", audio_quality="Dolby", release_date=date(2024, 3, 5))
    WebSeriesSubtitle.objects.create(web_series=ws1, language=Language.objects.get(language_code="PT"))

    for cc in ["US", "IN"]:
        WebSeriesCountry.objects.create(web_series=ws1, country=Country.objects.get(country_code=cc))

    Contract.objects.create(
        contract_id="C10",
        web_series=ws1,
        prod_house=ph1,
        contract_start_date=date(2024, 1, 1),
        contract_end_date=date(2026, 1, 1),
        per_episode_charge=18000,
        total_contract_value=54000,
        contract_status="Active"
    )

    Schedule.objects.create(schedule_id="SCH10", episode_id="E10", country_id="US", schedule_start_ts=datetime(2024, 3, 10, 18, 0), schedule_end_ts=datetime(2024, 3, 10, 19, 0), is_live_flag="Y")

    # ---------------------------------------------------------
    # WEB SERIES 2 — “Samurai Code” (Action)
    # ---------------------------------------------------------
    ws2 = WebSeries.objects.create(
        web_series_id="WS11",
        name="Samurai Code",
        no_of_episodes=2,
        language=Language.objects.get(language_code="JP_L"),
        release_date=date(2023, 9, 10),
        description="A rogue samurai rises against a corrupt shogunate.",
        producer_house=ph2,
        producer=pr2
    )

    WebSeriesType.objects.create(web_series=ws2, series_type=SeriesType.objects.get(series_type_id="T2"))

    Episode.objects.bulk_create([
        Episode(episode_id="E13", web_series=ws2, episode_number=1, episode_title="Fallen Honor", total_viewers=7000, tech_interruption_flag="N", duration_minutes=45),
        Episode(episode_id="E14", web_series=ws2, episode_number=2, episode_title="Rise of the Blade", total_viewers=7600, tech_interruption_flag="N", duration_minutes=50),
    ])

    WebSeriesDubbing.objects.create(web_series=ws2, language=Language.objects.get(language_code="EN"), dubbing_studio="Tokyo Soundworks", dubbing_artist="Kenji Ito", audio_quality="Dolby", release_date=date(2024, 1, 15))

    WebSeriesSubtitle.objects.create(web_series=ws2, language=Language.objects.get(language_code="PT"))

    for cc in ["JP", "US"]:
        WebSeriesCountry.objects.create(web_series=ws2, country=Country.objects.get(country_code=cc))

    Contract.objects.create(
        contract_id="C11",
        web_series=ws2,
        prod_house=ph2,
        contract_start_date=date(2023, 7, 1),
        contract_end_date=date(2025, 7, 1),
        per_episode_charge=25000,
        total_contract_value=50000,
        contract_status="Active"
    )

    Schedule.objects.create(schedule_id="SCH11", episode_id="E13", country_id="JP", schedule_start_ts=datetime(2024, 4, 1, 20, 0), schedule_end_ts=datetime(2024, 4, 1, 21, 0), is_live_flag="Y")

    # ---------------------------------------------------------
    # WEB SERIES 3 — “Laugh Factory” (Comedy)
    # ---------------------------------------------------------
    ws3 = WebSeries.objects.create(
        web_series_id="WS12",
        name="Laugh Factory",
        no_of_episodes=3,
        language=Language.objects.get(language_code="PT"),
        release_date=date(2022, 5, 20),
        description="Three friends start a sketch comedy channel.",
        producer_house=ph3,
        producer=pr3
    )

    WebSeriesType.objects.create(web_series=ws3, series_type=SeriesType.objects.get(series_type_id="T3"))

    Episode.objects.bulk_create([
        Episode(episode_id="E15", web_series=ws3, episode_number=1, episode_title="Sketch Gone Wrong", total_viewers=3500, tech_interruption_flag="N", duration_minutes=38),
        Episode(episode_id="E16", web_series=ws3, episode_number=2, episode_title="The Viral Hit", total_viewers=4100, tech_interruption_flag="N", duration_minutes=40),
        Episode(episode_id="E17", web_series=ws3, episode_number=3, episode_title="Late Night Chaos", total_viewers=4600, tech_interruption_flag="N", duration_minutes=42),
    ])

    WebSeriesDubbing.objects.create(web_series=ws3, language=Language.objects.get(language_code="EN"), dubbing_studio="Rio Dubs", dubbing_artist="Marco Silva", audio_quality="Stereo", release_date=date(2023, 2, 10))

    WebSeriesSubtitle.objects.create(web_series=ws3, language=Language.objects.get(language_code="HI"))

    for cc in ["BR", "IN"]:
        WebSeriesCountry.objects.create(web_series=ws3, country=Country.objects.get(country_code=cc))

    Contract.objects.create(
        contract_id="C12",
        web_series=ws3,
        prod_house=ph3,
        contract_start_date=date(2022, 4, 1),
        contract_end_date=date(2024, 4, 1),
        per_episode_charge=10000,
        total_contract_value=30000,
        contract_status="Expired"
    )

    Schedule.objects.create(schedule_id="SCH12", episode_id="E15", country_id="BR", schedule_start_ts=datetime(2024, 6, 10, 19, 0), schedule_end_ts=datetime(2024, 6, 10, 20, 0), is_live_flag="N")


    print("🌟 NEW BULK SEED DATA INSERTED SUCCESSFULLY!")