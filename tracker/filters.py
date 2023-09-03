from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from django.db import models

from .models import Shipment

class ShipmentFilter(FilterSet):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'carrier']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'iexact'
                }
            }
        }
