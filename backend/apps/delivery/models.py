from ckeditor_uploader.fields import RichTextUploadingField

from core.abstract_models import SeoModel, TimeStampedModel


class DeliveryPage(SeoModel, TimeStampedModel):
    description = RichTextUploadingField('Опис', blank=True)

    def __str__(self):
        return 'Сторінка "Доставка та оплата"'

    class Meta:
        verbose_name = 'Зміст сторінки "Доставка та оплата"'
        verbose_name_plural = 'Зміст сторінки "Доставка та оплата"'
