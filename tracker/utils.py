from django.conf import settings
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
        url = f'{self.COORDINATION_API}zip?zip={self.zip_code},{self.country_code}&appid={settings.OPEN_WEATHER_API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            return resp.json()
        raise requests.exceptions.ConnectionError
    
    def _get_current_forcast(self, coordinates):
        longitude = coordinates.get('lon')
        latitude = coordinates.get('lat')
        url = f'{self.LOCATION_API}?lat={latitude}&lon={longitude}&appid={self.API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            return resp.json().get('weather', {}).get('description', 'N/A')
        raise requests.exceptions.ConnectionError
