from django.db import models


class Shipment(models.Model):
    tracking_number = models.CharField(blank=False, null=False, max_length=10)
    carrier = models.CharField(blank=True, null=True, max_length=5)
    sender_address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='sender_address')
    receiver_address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='receiver_address')
    article_name = models.CharField(blank=True, null=False, default='undisclosed-item', max_length=128)
    article_quantity = models.IntegerField(blank=True, null=False, default=1)
    article_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    sku = models.CharField(blank=True, null=True, max_length=5)
    status = models.CharField(blank=True, null=False, default='inbound-scan', max_length=16)
    
    def __str__(self):
        return f"Item '{self.article_name}' with tracking-number '{self.tracking_number}' is in '{self.status}' status."


class Address(models.Model):
    class CountryChoices(models.TextChoices):
        FRANCE = 'France',
        BELGIUM = 'Belgium',
        SPAIN = 'Spain',
        NETHERLANDS = 'Netherlands',
        DENMARK = 'Denmark',
        GERMANY = 'Germany'

    country = models.CharField(blank=False, null=False, choices=CountryChoices.choices, max_length=16)
    city = models.CharField(blank=False, null=False, max_length=128)
    zip_code = models.CharField(blank=False, null=False, max_length=5)
    building_number = models.CharField(blank=True, null=True, max_length=16)
    street_name = models.CharField(blank=True, null=True, max_length=16)