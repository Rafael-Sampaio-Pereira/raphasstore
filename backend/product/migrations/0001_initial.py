# Generated by Django 4.1 on 2022-08-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("brand", models.CharField(blank=True, max_length=100, null=True)),
                ("sku", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("price", models.FloatField()),
                ("purchase_price", models.FloatField()),
            ],
            options={
                "ordering": [
                    "title",
                    "description",
                    "brand",
                    "sku",
                    "category",
                    "purchase_price",
                    "price",
                    "image",
                ],
            },
        ),
    ]
