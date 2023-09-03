from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
import requests
from django.conf import settings
from .models import Shipment
from .filters import ShipmentFilter
from .serializers import ShipmentSerializer

class TrackShipmentViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShipmentFilter


    def _get_coordinates(self, zip_code, country_code):
        url = f'{settings.LOCATION_COORDINATION_API}zip?zip={zip_code},{settings.COUNTRY_CODE_MAP.get(country_code)}&appid={settings.OPEN_WEATHER_API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            return resp.json()
        raise requests.exceptions.ConnectionError
    
    def _get_current_forcast(self, coordinates):
        longitude = coordinates.get('lon')
        latitude = coordinates.get('lat')
        url = f'{settings.LOCATION_FORCAST_API}?lat={latitude}&lon={longitude}&appid={settings.OPEN_WEATHER_API_KEY}'
        resp = requests.get(url)
        if resp.ok:
            return 
        
        