# Generated by Django 5.2.3 on 2025-06-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_catalogpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogpage',
            name='text_1',
        ),
    ]
