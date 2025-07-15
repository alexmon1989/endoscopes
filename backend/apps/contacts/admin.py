from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import ContactsSettings


class ContactsSettingsAdmin(SingleModelAdmin):
    """Класс для описания интерфейса администрирования модели CatalogPage."""
    fieldsets = (
        (None, {
            'fields': (
                'meta_h1',
                'phones',
                'email',
                'telegram_chat_id',
                'instagram_url',
                'facebook_url',
            )
        }),
        ('SEO опції', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


admin.site.register(ContactsSettings, ContactsSettingsAdmin)
