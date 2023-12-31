from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TrackShipmentViewSet

router = DefaultRouter()

router.register("track", TrackShipmentViewSet, basename="track_shipment")

urlpatterns = [path("", include(router.urls), name="api")]
