from django.db import models

from ckeditor.fields import RichTextField

from core.abstract_models import TimeStampedModel, SeoModel


class ContactsSettings(TimeStampedModel, SeoModel):
    phones = RichTextField('Телефон')
    email = RichTextField('Email')
    telegram_chat_id = models.PositiveIntegerField(
        'telegram_chat_id',
        null=True,
        blank=True,
        help_text='Ідентифікатор користувача Telegram, якому бот буде відправляти повідомлення.'
    )
    instagram_url = models.URLField('Instagram URL', null=True, blank=True)
    facebook_url = models.URLField('Facebook URL', null=True, blank=True)

    def __str__(self):
        return 'Зміст та налаштування сторінки'

    class Meta:
        verbose_name = 'Зміст та налаштування сторінки'
        verbose_name_plural = 'Зміст та налаштування сторінки'
