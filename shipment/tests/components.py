from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Address, Shipment


class TestTrackingAPI(APITestCase):
    def setUp(self) -> None:
        sender_address = Address.objects.create(
            country="Germany", city="Berlin", zip_code="10115", street_name="street 1"
        )
        receiver_address_1 = Address.objects.create(
            country="Spain", city="Madrid", zip_code="28013", street_name="street 5"
        )
        receiver_address_2 = Address.objects.create(
            country="France", city="Paris", zip_code="75001", street_name="street 10"
        )
        receiver_address_3 = Address.objects.create(
            country="Netherlands",
            city="Amsterdam",
            zip_code="1016",
            street_name="street 10",
        )

        Shipment.objects.bulk_create(
            [
                Shipment(
                    tracking_number="TN12345680",
                    carrier="DPD",
                    sender_address=sender_address,
                    receiver_address=receiver_address_1,
                    article_name="Keyboard",
                    article_quantity=1,
                    article_price=50,
                    sku="KB012",
                    status="delivery",
                ),
                Shipment(
                    tracking_number="TN12345670",
                    carrier="DHL",
                    sender_address=sender_address,
                    receiver_address=receiver_address_2,
                    article_name="Mouse",
                    article_quantity=10,
                    article_price=80,
                    sku="MD012",
                    status="in_transit",
                ),
                Shipment(
                    tracking_number="TN12345670",
                    carrier="FedEx",
                    sender_address=sender_address,
                    receiver_address=receiver_address_3,
                    article_name="Laptop",
                    article_quantity=1,
                    article_price=900,
                    sku="CG012",
                    status="inbound_scan",
                ),
            ]
        )

    def test_get_all_available_shipments_success(self):
        resp = self.client.get(reverse("track_shipment-list"))
        self.assertEqual(len(resp.json()), 3)
        response_content = resp.json()
        for content in response_content:
            self.assertIn(content.get("carrier"), ["DPD", "DHL", "FedEx"])

    def test_get_incorrect_shipment(self):
        resp = self.client.get(f"{reverse('track_shipment-list')}?carrier=bad-value")
        self.assertEqual(len(resp.json()), 0)
        self.assertEqual(resp.json(), [])

    def test_get_shipments_by_carrier_success(self):
        resp = self.client.get(f"{reverse('track_shipment-list')}?carrier=dhl")
        self.assertEqual(len(resp.json()), 1)
        self.assertEqual(resp.json()[0].get("carrier"), "DHL")

    def test_get_shipments_by_tracking_number(self):
        resp = self.client.get(
            f"{reverse('track_shipment-list')}?tracking_number=TN12345680"
        )
        self.assertEqual(len(resp.json()), 1)
        self.assertEqual(resp.json()[0].get("tracking_number"), "TN12345680")

    def test_get_shipments_by_carrier_and_tracking_number(self):
        resp = self.client.get(
            f"{reverse('track_shipment-list')}?carrier=fedex&tracking_number=TN12345670"
        )
        self.assertEqual(len(resp.json()), 1)
        self.assertEqual(resp.json()[0].get("tracking_number"), "TN12345670")
        self.assertEqual(resp.json()[0].get("carrier"), "FedEx")
