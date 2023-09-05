from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from .models import Shipment
from .filters import ShipmentFilter
from .serializers import ShipmentSerializer


class TrackShipmentViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    http_method_names = ["get"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShipmentFilter
