# Generated by Django 4.0.2 on 2023-02-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_alter_realtor_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.IntegerField(),
        ),
    ]
