# Generated by Django 4.0.2 on 2023-02-17 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0006_alter_advertisement_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
            options={
                'verbose_name_plural': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='address',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='apartment',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='house',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='street',
            field=models.CharField(default=1, max_length=63),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisement.city'),
            preserve_default=False,
        ),
    ]