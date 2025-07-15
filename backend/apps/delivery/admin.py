from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import DeliveryPage


class DeliveryPageAdmin(SingleModelAdmin):
    """Класс для описания интерфейса администрирования модели CatalogPage."""
    fieldsets = (
        (None, {
            'fields': (
                'meta_h1',
                'description',
            )
        }),
        ('SEO опції', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


admin.site.register(DeliveryPage, DeliveryPageAdmin)
