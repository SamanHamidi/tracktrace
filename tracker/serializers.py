from rest_framework import serializers

from .models import Shipment, Address
from .utils import ForcastUtility

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = [id]


class ShipmentSerializer(serializers.ModelSerializer):
    sender_address = AddressSerializer()
    receiver_address = AddressSerializer()
    destination_forcast = serializers.SerializerMethodField()
    class Meta:
        model = Shipment
        exclude = ['id']

    def get_destination_forcast(self, obj):
        return ForcastUtility(obj).forcast()