# Generated by Django 5.0.2 on 2024-02-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0004_alter_product_drive_unit_alter_product_type_of_fuel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='car_year',
            field=models.PositiveIntegerField(default='', verbose_name='Год машины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Обьём двигателя'),
        ),
    ]
