# Generated by Django 4.2.4 on 2023-09-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=10)),
                ('carrier', models.CharField(blank=True, choices=[('DHL', 'Dhl'), ('UPS', 'Ups'), ('DPD', 'Dpd'), ('FedEx', 'Fdx'), ('GLS', 'Gls')], max_length=5, null=True)),
                ('sender_address', models.TextField()),
                ('receiver_address', models.TextField()),
                ('article_name', models.CharField(blank=True, default='Undisclosed Item', max_length=128)),
                ('article_quantity', models.IntegerField(blank=True, default=1)),
                ('article_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sku', models.CharField(blank=True, max_length=5, null=True)),
                ('status', models.CharField(blank=True, choices=[('In Transit', 'In Transit'), ('Inbound Scan', 'Inbound Scan'), ('Delivery', 'Delivery'), ('Scanned', 'Scanned')], default='Inbound Scan', max_length=16)),
            ],
        ),
    ]