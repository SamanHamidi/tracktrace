from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .models import Shipment
from .filters import ShipmentFilter
from .serializers import ShipmentSerializer
# Create your views here.

class TrackShipmentViewSet(RetrieveModelMixin, GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = ShipmentFilter
