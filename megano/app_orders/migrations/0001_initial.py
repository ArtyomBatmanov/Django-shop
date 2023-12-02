# Generated by Django 4.2.1 on 2023-12-02 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_users", "0001_initial"),
        ("app_products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                    "createdAt",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "deliveryType",
                    models.CharField(
                        default="", max_length=128, verbose_name="тип доставки"
                    ),
                ),
                (
                    "paymentType",
                    models.CharField(
                        default="", max_length=128, verbose_name="тип оплаты"
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="сумма заказа",
                    ),
                ),
                (
                    "status",
                    models.CharField(default="", max_length=128, verbose_name="статус"),
                ),
                (
                    "city",
                    models.CharField(default="", max_length=256, verbose_name="город"),
                ),
                (
                    "address",
                    models.CharField(default="", max_length=256, verbose_name="адрес"),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="orders",
                        to="app_products.product",
                        verbose_name="продуты",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="app_users.profile",
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="CountProductinOrder",
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
                ("count", models.PositiveIntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="app_products.product",
                    ),
                ),
            ],
        ),
    ]