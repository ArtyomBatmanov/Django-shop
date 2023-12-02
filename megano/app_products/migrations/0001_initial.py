# Generated by Django 4.2.1 on 2023-12-02 21:30

import app_products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_catalog", "0001_initial"),
    ]

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
                ("title", models.CharField(max_length=128)),
                ("description", models.CharField(blank=True, max_length=256)),
                ("fullDescription", models.TextField(blank=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("count", models.IntegerField(default=0)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("freeDelivery", models.BooleanField(default=True)),
                ("limited_edition", models.BooleanField(default=False)),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0, max_digits=3),
                ),
                ("active", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="app_catalog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(blank=True, max_length=128)),
                (
                    "product",
                    models.ManyToManyField(
                        related_name="tags",
                        to="app_products.product",
                        verbose_name="product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Sale",
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
                    "salePrice",
                    models.DecimalField(
                        db_index=True, decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("dateFrom", models.DateField(default="")),
                ("dateTo", models.DateField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sales",
                        to="app_products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sale",
                "verbose_name_plural": "Sales",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("author", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=256)),
                ("text", models.TextField()),
                ("rate", models.PositiveSmallIntegerField(default=5)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="app_products.product",
                        verbose_name="product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="ProductSpecification",
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
                ("name", models.CharField(default="", max_length=256)),
                ("value", models.CharField(default="", max_length=256)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="specifications",
                        to="app_products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product specification",
                "verbose_name_plural": "Product specifications",
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("name", models.CharField(blank=True, max_length=128)),
                (
                    "image",
                    models.FileField(
                        upload_to=app_products.models.product_image_directory_path
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="app_products.product",
                        verbose_name="product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product image",
                "verbose_name_plural": "Product images",
                "ordering": ["pk"],
            },
        ),
    ]
