# Generated by Django 4.2.1 on 2023-06-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(default=""),
        ),
    ]
