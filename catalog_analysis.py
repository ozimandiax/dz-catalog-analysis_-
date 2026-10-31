import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
     "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
     "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    avrg = 0
    for m in movies:
        avrg += m["rating"]
    avrg /= len(movies)
    return round(avrg, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for m in movies:
        ages.append(current_year - m["year"])
    newest = min(ages)
    oldest = max(ages)
    average = math.ceil(sum(ages) / len(ages))
    return oldest, newest, average


def duration_in_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}ч {minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


for m in movies:
    if "comedy" in m["genres"]:
        continue
    print(m["title"])


for catalog in (movies, movies[:7]):
    i = 0
    while i < len(catalog):
        if catalog[i]["rating"] > 9:
            print(catalog[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    m_count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            m_count += 1
    return m_count


def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    top = []

    for m in sorted_movies[:n]:
        top.append((m["title"], m["rating"]))

    return top


def count_by_genre(movies):
    counts = {}
    for m in movies:
        for genre in m["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for m in movies:
        for actor in m["actors"]:
            filmography[actor] = filmography.get(actor, []) + [m["title"]]
    return filmography


average = average_rating(movies)
above_average_movies = {movie["title"]: movie["rating"]
                        for movie in movies if movie["rating"] > average}


def all_genres(movies):
    genres = set()

    for m in movies:
        genres.update(m["genres"])

    return genres


def common_actors(movie1, movie2):
    actors = set(movie1["actors"]) & set(movie2["actors"])
    return actors


def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    genres_b = set()
    for m in movies_a:
        genres_a.update(m["genres"])
    for m in movies_b:
        genres_b.update(m["genres"])
    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m


for movie in iter_high_rated(movies):
    print(format_report_line(movie))


total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)

