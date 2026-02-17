import requests


class WeatherForecast:
    def __init__(self, cache_file="rain_cache.txt",
                 latitude = 53.3331, longitude = -6.2489):
        self.cache_file = cache_file
        self.latitude = latitude
        self.longitude = longitude
        self._cache = self._load_cache()

    def _load_cache(self):

        cache = {}
        try:
            with open(self.cache_file, "r") as fd:
                lines = fd.read().strip().splitlines()
                for line in lines:
                    parts = line.split(",")
                    if len(parts) == 2:
                        cache[parts[0]] = float(parts[1])
        except FileNotFoundError:
            pass
        except Exception:
            pass
        return cache

    def _get_precip(self, date_str):

        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
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

    def _save_to_cache(self):
        try:
            with open(self.cache_file, "w") as fd:
                for date_str, value in self._cache.items():
                    fd.write(f"{date_str},{value}\n")
        except OSError:
            print("Failed to write cache")

    def __setitem__(self, date_str, value):
        self._cache[date_str] = value
        self._save_to_cache()

    def __getitem__(self, date_str):
        if date_str not in self._cache:
            precip = self._get_precip(date_str)
            self._cache[date_str] = precip
            self._save_to_cache()
        return self._cache[date_str]

    def __iter__(self):
        return iter(self._cache)

    def items(self):
        for date, value in self._cache.items():
            yield (date, value)