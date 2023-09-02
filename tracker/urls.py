from django.urls import path, include
from .views import TrackShipmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('shipment', TrackShipmentViewSet, basename='track_shipment')

urlpatterns = [
    path('', include(router.urls))
]