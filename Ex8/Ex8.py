import requests
from datetime import datetime, timedelta

cache_file = "rain_cache.txt"

#Default latitude and longitude from Dublin, IE

latitude = 53.3331
longitude = -6.2489

def load_cache():

    try:
        with open(cache_file, "r") as fd:
            lines = fd.read().strip().splitlines()
            cache = {line.split(",")[0]: float(line.split(",")[1]) for line in lines}
            return cache
    except FileNotFoundError:
        return {}
    except Exception:
        return {}

def save_to_cache(date_str, value):

    try:
        with open(cache_file, "a") as fd:
            fd.write(f"{date_str},{value}\n")
    except OSError:
        print("Failed to write cache")

def get_next_day():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.strftime("%Y-%m-%d")

def validate_or_default(date_input):

    if not date_input:
        return get_next_day()

    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        print("Invalid format, using next dat")
        return get_next_day()

def get_precip(date_str):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&daily=precipitation_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date_str}"
        f"&end_date={date_str}"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        values = data.get("daily", {}).get("precipitation_sum", [])
        if not values:
            return None
        return float(values[0])
    except Exception:
        print("API request failed")
        return None

def interpret_precip(p):

    if p is None or p<0:
        return "I dont know"
    if p == 0:
        return "It will not rain"
    if p > 0:
        return "It will rain"

    return "Unknown or invalid"

def main():
    cache = load_cache()

    user_date = input("Enter date (YYYY-MM-DD): or press enter for next day: ").strip()
    date_str = validate_or_default(user_date)

    if date_str in cache:
        precip = cache[date_str]
        print("Cached")
    else:
        precip = get_precip(date_str)
        save_to_cache(date_str, precip)

    print(date_str, ":", interpret_precip(precip))

if __name__ == "__main__":
    main()