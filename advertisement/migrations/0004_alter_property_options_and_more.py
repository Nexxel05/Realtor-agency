# Generated by Django 4.0.2 on 2023-02-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_alter_address_apartment_alter_address_house'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['name'], 'verbose_name_plural': 'properties'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]