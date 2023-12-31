# Generated by Django 4.2.4 on 2023-09-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("France", "France"),
                            ("Belgium", "Belgium"),
                            ("Spain", "Spain"),
                            ("Netherlands", "Netherlands"),
                            ("Denmark", "Denmark"),
                            ("Germany", "Germany"),
                        ],
                        max_length=16,
                    ),
                ),
                ("city", models.CharField(max_length=128)),
                ("zip_code", models.CharField(max_length=5)),
                (
                    "building_number",
                    models.CharField(blank=True, max_length=16, null=True),
                ),
                ("street_name", models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Shipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tracking_number", models.CharField(max_length=10)),
                ("carrier", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "article_name",
                    models.CharField(
                        blank=True, default="undisclosed-item", max_length=128
                    ),
                ),
                ("article_quantity", models.IntegerField(blank=True, default=1)),
                (
                    "article_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("sku", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "status",
                    models.CharField(blank=True, default="inbound-scan", max_length=16),
                ),
                (
                    "receiver_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver_address",
                        to="shipment.address",
                    ),
                ),
                (
                    "sender_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender_address",
                        to="shipment.address",
                    ),
                ),
            ],
        ),
    ]
