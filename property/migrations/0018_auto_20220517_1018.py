# Generated by Django 2.2.24 on 2022-05-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220517_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
