from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .models import Shipment
from .serializers import ShipmentSerializer
# Create your views here.

class TrackShipmentViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    # http_method_names = ['get']