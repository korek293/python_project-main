import time
import requests
from requests.exceptions import RequestException
API_KEY = "PQOKCKLAS"

def retry(func):
    def wrapper_retry(*aqrgs, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*aqrgs, **kwargs)
            except RequestException:
                print(f"Faild to get data. Retrying in {seconds}")
                time.sleep(seconds)
        return func(*aqrgs, **kwargs)
    return wrapper_retry

@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}"
    response = requests.get(url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours

def fahrenheit_to_celsius(*, fahrenheit_temp: float) -> int:
    return round((fahrenheit_temp -32) * 5 / 9)


def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp=weather["temp"])
        if uvindex >=3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celsius_temp})
    return dangerous_hours


date = "2023-08-04"
city = "London, UK"
weather_by_hour = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hour=weather_by_hour)
print(dangerous_hours)