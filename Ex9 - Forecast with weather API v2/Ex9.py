from datetime import datetime, timedelta
from WeatherForecast import WeatherForecast

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
        print("Invalid format, using next day")
        return get_next_day()

def interpret_precip(p):

    if p is None or p<0:
        return "I dont know"
    if p == 0:
        return "It will not rain"
    if p > 0:
        return "It will rain"

    return "Unknown or invalid"

def main():

    weather_forecast = WeatherForecast()

    user_date = input("Enter date (YYYY-MM-DD): or press enter for next day: ").strip()
    date_str = validate_or_default(user_date)

    precip = weather_forecast[date_str]

    print(date_str, ":", interpret_precip(precip))

    print("\nSaved forecast dates: ")
    for date in weather_forecast:
        print(date)

    print("\nSaved forecast values: ")
    for date, value in weather_forecast.items():
        print(value)

if __name__ == "__main__":
    main()