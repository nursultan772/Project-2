# Generated by Django 5.0.2 on 2024-02-20 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='checkpoint',
            field=models.CharField(choices=[('автомат', 'автомат'), ('механика', 'механика')], default='автомат', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='drive_unit',
            field=models.CharField(choices=[('передний привод', 'передний привод'), ('задний привод', 'задний привод'), ('полный привод', 'полный привод')], default='передний привод', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='type_of_fuel',
            field=models.CharField(choices=[('бензин', 'бензин'), ('дизель', 'дизель'), ('газ', 'газ'), ('электро', 'электро')], default='передний привод', max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='car_body',
            field=models.TextField(verbose_name='Тип машины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='car_year',
            field=models.DateField(default='', verbose_name='Год машины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazin.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mileage',
            field=models.PositiveIntegerField(verbose_name='Пробег машины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Название машины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='post_time',
            field=models.DateTimeField(verbose_name='Время поста'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена автомобиля'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.IntegerField(verbose_name='Обьём двигателя'),
        ),
    ]