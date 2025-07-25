# Generated by Django 5.2.3 on 2025-07-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactssettings_telegram_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactssettings',
            name='facebook_url',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='contactssettings',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
    ]
