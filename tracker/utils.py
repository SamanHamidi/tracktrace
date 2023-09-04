from django.conf import settings
from django.core.cache import cache

import requests


class ForcastUtility:
    API_KEY = settings.OPEN_WEATHER_API_KEY
    COORDINATION_API = settings.LOCATION_COORDINATION_API
    LOCATION_API = settings.LOCATION_FORCAST_API
    
    def __init__(self, obj) -> None:
        self.country_code = settings.COUNTRY_CODE_MAP.get(obj.country)
        self.zip_code = obj.zip_code
    
    def forcast(self):
        coordinates = self._get_coordinates()
        return self._get_current_forcast(coordinates)
    
    def _get_coordinates(self):
        if cached_coordinates := cache.get(f'{self.zip_code}:{self.country_code}', False):
            return cached_coordinates
        
        url = f'{self.COORDINATION_API}zip?zip={self.zip_code},{self.country_code}&appid={settings.OPEN_WEATHER_API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            coordinates = resp.json()
            cache.set(f'{self.zip_code}:{self.country_code}', coordinates, None)
            return coordinates
        raise requests.exceptions.ConnectionError
    
    def _get_current_forcast(self, coordinates):
        latitude = coordinates.get('lat')
        longitude = coordinates.get('lon')
        
        if cached_forcast := cache.get(f'{latitude}:{longitude}', False):
            return cached_forcast

        url = f'{self.LOCATION_API}?lat={latitude}&lon={longitude}&appid={self.API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            forcast = resp.json().get('weather', {}).get('description', 'N/A')
            cache.set(f'{latitude}:{longitude}', forcast, 2*3600)
            return forcast
        raise requests.exceptions.ConnectionError
