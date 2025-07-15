from django.db import models


class SeoModel(models.Model):
    """Абстрактний клас моделі, що містить опис SEO-тегів."""
    meta_h1 = models.CharField('Тег h1 (мета-тег)', max_length=255, null=True, blank=True)
    meta_title = models.CharField('Title (мета-тег)', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField('Keywords (мета-тег)', max_length=255, null=True, blank=True)
    meta_description = models.TextField('Description (мета-тег)', null=True, blank=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """Абстрактний клас моделі, що містить поля created, updated_at."""
    created_at = models.DateTimeField('Створено', auto_now_add=True)
    updated_at = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        abstract = True
