# Generated by Django 5.0.2 on 2024-02-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0005_alter_product_car_year_alter_product_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='horse_power',
            field=models.PositiveIntegerField(default=0, verbose_name='Сколько лошадек'),
        ),
    ]
