from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TrackShipmentViewSet

router = DefaultRouter()

router.register('track', TrackShipmentViewSet, basename='track_shipment')

urlpatterns = [
    path('api/v1/shipment/', include(router.urls), name='api')
]