# Generated by Django 5.2.3 on 2025-06-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег h1 (мета-тег)')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title (мета-тег)')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords (мета-тег)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description (мета-тег)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
