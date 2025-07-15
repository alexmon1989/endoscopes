from django import template

from apps.catalog.services import category_get_all_items_enabled_qs
from apps.contacts.models import ContactsSettings


register = template.Library()


@register.simple_tag
def categories() -> list[dict]:
    return category_get_all_items_enabled_qs().values('title', 'slug')


@register.simple_tag
def contacts() -> list[dict]:
    return ContactsSettings.objects.all().first()
