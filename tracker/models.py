from django.db import models

# Create your models here.


class Shipment(models.Model):
    class CarrierChoices(models.TextChoices):
        DHL = "DHL"
        UPS = "UPS"
        DPD = "DPD"
        FDX = "FedEx"
        GLS = "GLS"
        
    class DeliveryStatusChoices(models.TextChoices):
        IN_TRANSIT = "In Transit"
        INBOUND_SCAN = "Inbound Scan"
        DELIVERY = "Delivery"
        SCANNED = "Scanned"

    tracking_number = models.CharField(blank=False, null=False, max_length=10)
    carrier = models.CharField(blank=True, null=True, choices=CarrierChoices.choices, max_length=5)
    sender_address = models.TextField(blank=False, null=False)
    receiver_address = models.TextField(blank=False, null=False)
    article_name = models.CharField(blank=True, null=False, default='undisclosed item', max_length=128)
    article_quantity = models.IntegerField(blank=True, null=False, default=1)
    article_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    sku = models.CharField(blank=True, null=True, max_length=5)
    status = models.CharField(blank=True, null=False, choices=DeliveryStatusChoices.choices, default=DeliveryStatusChoices.INBOUND_SCAN, max_length=16)
    
    def __str__(self):
        return f"Item '{self.article_name}' with tracking-number '{self.tracking_number}' is in '{self.status}' status."
    