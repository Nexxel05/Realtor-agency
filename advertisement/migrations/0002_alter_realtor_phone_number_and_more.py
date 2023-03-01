# Generated by Django 4.0.2 on 2023-02-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='years_of_experience',
            field=models.IntegerField(null=True),
        ),
    ]
