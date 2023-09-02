from rest_framework.serializers import ModelSerializer
from .models import Shipment

class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = Shipment
