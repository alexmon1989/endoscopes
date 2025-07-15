from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import HomePage


class HomeAdmin(SingleModelAdmin):
    """Класс для описание интерфейса администрирования модели HomeAdmin."""
    fieldsets = (
        (None, {
            'fields': (
                'meta_h1',
                'text_1',
                'description',
            )
        }),
        ('SEO опції', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


admin.site.register(HomePage, HomeAdmin)
