from django_filters.rest_framework import FilterSet
from .models import Shipment

class ShipmentFilter(FilterSet):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'carrier']
