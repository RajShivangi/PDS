from datetime import date, datetime, timedelta
import random

from core.models import (
    Country,
    Language,
    ProductionHouse,
    Producer,
    WebSeries,
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


def run():
    # -------------------------------
    # 1. Base Countries & Languages
    # -------------------------------
    country_data = {
        "US": "United States",
        "IN": "India",
        "UK": "United Kingdom",
        "JP": "Japan",
        "BR": "Brazil",
    }

    for code, name in country_data.items():
        Country.objects.get_or_create(
            country_code=code,
            defaults={"country_name": name},
        )

    language_data = {
        "EN": "English",
        "HI": "Hindi",
        "JP_L": "Japanese",
        "ES": "Spanish",
        "FR": "French",
    }

    for code, name in language_data.items():
        Language.objects.get_or_create(
            language_code=code,
            defaults={"country_name": name},
        )

    # -------------------------------
    # 2. Production Houses & Producers
    # -------------------------------
    ph_defs = [
        ("PH201", "Starlight Studios", "Los Angeles", "CA", "US"),
        ("PH202", "Mystic Reel Productions", "London", "London", "UK"),
        ("PH203", "Dreamscape Entertainment", "New York", "NY", "US"),
        ("PH204", "Aurora Pictures", "Mumbai", "MH", "IN"),
        ("PH205", "Neon Wave Media", "Tokyo", "Tokyo", "JP"),
    ]

    prod_houses = {}
    for ph_id, ph_name, city, state, ccode in ph_defs:
        country = Country.objects.get(country_code=ccode)
        ph, _ = ProductionHouse.objects.get_or_create(
            production_house_id=ph_id,
            defaults={
                "prod_house_name": ph_name,
                "street": "Main Street",
                "city": city,
                "state": state,
                "country": country,
                "zipcode": "00000",
                "year_established": 2000,
            },
        )
        prod_houses[ph_id] = ph

    producer_defs = [
        ("PR201", "Lena Hart", "US"),
        ("PR202", "Raj Malhotra", "IN"),
        ("PR203", "Kenji Morita", "JP"),
        ("PR204", "Amelia Frost", "UK"),
        ("PR205", "Carlos Rivera", "BR"),
    ]

    producers = {}
    for pid, pname, ccode in producer_defs:
        country = Country.objects.get(country_code=ccode)
        p, _ = Producer.objects.get_or_create(
            producer_id=pid,
            defaults={
                "producer_name": pname,
                "city": "City",
                "state": "State",
                "country": country,
            },
        )
        producers[pid] = p

    # -------------------------------
    # 3. Viewer Accounts & Subscriptions (for Feedback)
    # -------------------------------
    v1, _ = ViewerAccount.objects.get_or_create(
        account_id="ACC100",
        defaults={
            "name": "Alice Viewer",
            "email": "alice@example.com",
            "city": "New York",
            "state": "NY",
            "country": Country.objects.get(country_code="US"),
        },
    )

    v2, _ = ViewerAccount.objects.get_or_create(
        account_id="ACC101",
        defaults={
            "name": "Ravi Viewer",
            "email": "ravi@example.com",
            "city": "Mumbai",
            "state": "MH",
            "country": Country.objects.get(country_code="IN"),
        },
    )

    Subscription.objects.get_or_create(
        subscription_id="SUB100",
        defaults={
            "account": v1,
            "plan_type": "Premium",
            "start_date": date(2023, 1, 1),
        },
    )

    Subscription.objects.get_or_create(
        subscription_id="SUB101",
        defaults={
            "account": v2,
            "plan_type": "Standard",
            "start_date": date(2023, 6, 1),
        },
    )

    # -------------------------------
    # 4. Web Series Definitions (your 10 franchise-style shows)
    # -------------------------------
    series_definitions = [
        # id, name, language_code, prod_house_id, producer_id, base_date, desc, available_countries, dubbings, subtitles
        (
            "WS201",
            "Arcane Academy",
            "EN",
            "PH201",
            "PR201",
            date(2023, 1, 10),
            "A group of gifted teens at a secret academy must protect the realm from awakening dark magic.",
            ["US", "UK", "IN"],
            ["HI", "FR"],
            ["EN", "HI", "FR"],
        ),
        (
            "WS202",
            "Children of the Rift",
            "EN",
            "PH203",
            "PR204",
            date(2023, 3, 5),
            "Kids in a quiet town discover a rift to another dimension and strange powers within themselves.",
            ["US", "UK"],
            ["ES"],
            ["EN", "ES"],
        ),
        (
            "WS203",
            "Flatmates Forever",
            "EN",
            "PH203",
            "PR201",
            date(2023, 4, 20),
            "Six young professionals navigate love, work, and chaos in shared apartments in the city.",
            ["US", "UK", "IN"],
            ["HI"],
            ["EN", "HI"],
        ),
        (
            "WS204",
            "Nightfall City",
            "EN",
            "PH202",
            "PR204",
            date(2023, 6, 1),
            "A detective teams up with an immortal night-spirit to solve supernatural crimes.",
            ["US", "UK"],
            ["FR"],
            ["EN", "FR"],
        ),
        (
            "WS205",
            "Echoes of the Future",
            "EN",
            "PH201",
            "PR205",
            date(2023, 7, 15),
            "A scientist sends memories back in time, fracturing reality as people recall events that never happened.",
            ["US", "BR", "UK"],
            ["ES", "FR"],
            ["EN", "ES", "FR"],
        ),
        (
            "WS206",
            "Royal Heirs",
            "EN",
            "PH204",
            "PR202",
            date(2023, 9, 1),
            "Three rival houses vie for the throne in a kingdom held together by fragile alliances.",
            ["IN", "UK"],
            ["HI"],
            ["EN", "HI"],
        ),
        (
            "WS207",
            "Neon Pulse",
            "EN",
            "PH205",
            "PR203",
            date(2023, 10, 10),
            "In a cyberpunk city, a rogue hacker uncovers a government mind-control program.",
            ["US", "JP"],
            ["JP_L"],
            ["EN", "JP_L"],
        ),
        (
            "WS208",
            "Beyond the Veil",
            "EN",
            "PH202",
            "PR204",
            date(2023, 11, 20),
            "A clairvoyant joins a secret society of ghost-hunters to break her family's curse.",
            ["US", "UK", "IN"],
            ["HI"],
            ["EN", "HI"],
        ),
        (
            "WS209",
            "The Perfect Matchers",
            "EN",
            "PH204",
            "PR202",
            date(2024, 1, 5),
            "A data analyst builds a matchmaking startup, only to be matched with her best friend.",
            ["US", "IN"],
            ["HI"],
            ["EN", "HI"],
        ),
        (
            "WS210",
            "Stardust Voyagers",
            "EN",
            "PH201",
            "PR205",
            date(2024, 2, 18),
            "A misfit crew explores uncharted galaxies searching for ancient artifacts.",
            ["US", "UK", "BR", "JP"],
            ["ES", "JP_L"],
            ["EN", "ES", "JP_L"],
        ),
    ]

    # -------------------------------
    # 5. Create Web Series + Episodes + Dubbing + Subtitles + Country + Contracts + Feedback + Schedule
    # -------------------------------
    episode_id_counter = 300
    schedule_id_counter = 400
    created_count = 0

    for ws_id, name, lang_code, ph_id, prod_id, base_date, desc, avail_ccodes, dubb_lang_codes, subtitle_lang_codes in series_definitions:
        lang = Language.objects.get(language_code=lang_code)
        ph = prod_houses[ph_id]
        prod = producers[prod_id]

        # 3 or 4 episodes
        num_episodes = random.choice([3, 4])

        ws, created = WebSeries.objects.get_or_create(
            web_series_id=ws_id,
            defaults={
                "name": name,
                "no_of_episodes": num_episodes,
                "language": lang,
                "release_date": base_date,
                "description": desc,
                "producer_house": ph,
                "producer": prod,
            },
        )

        if created:
            created_count += 1

        # Episodes
        episodes = []
        for ep_no in range(1, num_episodes + 1):
            episode_id = f"E{episode_id_counter}"
            episode_id_counter += 1

            ep, _ = Episode.objects.get_or_create(
                episode_id=episode_id,
                defaults={
                    "web_series": ws,
                    "episode_number": ep_no,
                    "episode_title": f"{name} - Episode {ep_no}",
                    "schedule_start_ts": datetime.combine(
                        base_date + timedelta(days=ep_no),
                        datetime.min.time(),
                    ),
                    "schedule_end_ts": datetime.combine(
                        base_date + timedelta(days=ep_no),
                        datetime.min.time(),
                    ) + timedelta(minutes=45),
                    "total_viewers": random.randint(5000, 25000),
                    "tech_interruption_flag": "N",
                    "duration_minutes": random.choice([35, 40, 45, 50]),
                },
            )
            episodes.append(ep)

        # Dubbing
        for d_code in dubb_lang_codes:
            d_lang = Language.objects.get(language_code=d_code)
            WebSeriesDubbing.objects.get_or_create(
                web_series=ws,
                language=d_lang,
                defaults={
                    "dubbing_studio": "Global Dubbing Studio",
                    "dubbing_artist": "Voice Artist",
                    "audio_quality": "Dolby",
                    "release_date": base_date + timedelta(days=60),
                },
            )

        # Subtitles
        for s_code in subtitle_lang_codes:
            s_lang = Language.objects.get(language_code=s_code)
            WebSeriesSubtitle.objects.get_or_create(
                web_series=ws,
                language=s_lang,
            )

        # Country Availability
        for ccode in avail_ccodes:
            ctry = Country.objects.get(country_code=ccode)
            WebSeriesCountry.objects.get_or_create(
                web_series=ws,
                country=ctry,
            )

        # Contract
        per_episode_charge = random.choice([15000, 20000, 25000])
        total_contract_value = per_episode_charge * num_episodes

        Contract.objects.get_or_create(
            contract_id=f"CON{ws_id[2:]}",
            defaults={
                "web_series": ws,
                "prod_house": ph,
                "contract_start_date": base_date - timedelta(days=60),
                "contract_end_date": base_date + timedelta(days=365),
                "per_episode_charge": per_episode_charge,
                "total_contract_value": total_contract_value,
                "contract_status": "Active",
            },
        )

        # Feedback – one from each viewer, on the series as a whole
        Feedback.objects.get_or_create(
            account=v1,
            web_series=ws,
            defaults={
                "feedback_text": f"Really enjoyed watching {name}!",
                "rating": random.randint(4, 5),
                "feedback_date": date.today(),
            },
        )

        Feedback.objects.get_or_create(
            account=v2,
            web_series=ws,
            defaults={
                "feedback_text": f"{name} had an interesting storyline.",
                "rating": random.randint(3, 5),
                "feedback_date": date.today(),
            },
        )

        # Schedule – schedule first episode in each available country
        first_ep = episodes[0]
        for ccode in avail_ccodes:
            ctry = Country.objects.get(country_code=ccode)
            schedule_id = f"SCH{schedule_id_counter}"
            schedule_id_counter += 1
            Schedule.objects.get_or_create(
                schedule_id=schedule_id,
                defaults={
                    "episode": first_ep,
                    "country": ctry,
                    "schedule_start_ts": first_ep.schedule_start_ts,
                    "schedule_end_ts": first_ep.schedule_end_ts,
                    "is_live_flag": "Y",
                },
            )

    print(f"✅ Seeded {created_count} new WebSeries with episodes, dubbing, subtitles, contracts, feedback, and schedules.")