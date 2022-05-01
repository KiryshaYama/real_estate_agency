# Generated by Django 2.2.24 on 2022-05-01 05:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220501_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]