# Generated by Django 4.0.4 on 2022-08-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_food_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulotlar',
            name='narhi',
            field=models.FloatField(max_length=20),
        ),
    ]
