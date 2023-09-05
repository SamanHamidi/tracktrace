from django.conf import settings
from django.core.cache import cache

import requests


class ForcastUtility:
    API_KEY = settings.OPEN_WEATHER_API_KEY
    COORDINATION_API = settings.LOCATION_COORDINATION_API
    LOCATION_API = settings.LOCATION_FORCAST_API

    def __init__(self, country, zip_code) -> None:
        self.country_code = settings.COUNTRY_CODE_MAP.get(country)
        self.zip_code = zip_code

    def forcast(self):
        coordinates = self._get_coordinates()
        return self._get_current_forcast(coordinates)

    def _get_coordinates(self):
        if cached_coordinates := cache.get(
            key=f"{self.zip_code}:{self.country_code}", default=False
        ):
            return cached_coordinates

        url = f"{self.COORDINATION_API}zip?zip={self.zip_code},{self.country_code}&appid={settings.OPEN_WEATHER_API_KEY}"
        resp = requests.get(url)
        if resp.ok:
            coordinates = resp.json()
            cache.set(
                key=f"{self.zip_code}:{self.country_code}",
                value=coordinates,
                timeout=None,
            )
            return coordinates

    def _get_current_forcast(self, coordinates):
        if not coordinates:
            return "N/A"

        latitude = coordinates.get("lat")
        longitude = coordinates.get("lon")
        if cached_forcast := cache.get(key=f"{latitude}:{longitude}", default=False):
            return cached_forcast

        url = f"{self.LOCATION_API}?lat={latitude}&lon={longitude}&appid={self.API_KEY}"
        resp = requests.get(url)
        if resp.ok:
            forcast = resp.json().get("weather", [{}])[0].get("description", "N/A")
            cache.set(key=f"{latitude}:{longitude}", value=forcast, timeout=2 * 3600)
            return forcast
        return "N/A"
