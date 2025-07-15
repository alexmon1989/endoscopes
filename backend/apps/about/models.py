from ckeditor_uploader.fields import RichTextUploadingField

from core.abstract_models import SeoModel, TimeStampedModel


class AboutPage(SeoModel, TimeStampedModel):
    description = RichTextUploadingField('Опис', blank=True)

    def __str__(self):
        return 'Сторінка "Про нас"'

    class Meta:
        verbose_name = 'Зміст сторінки "Про нас"'
        verbose_name_plural = 'Зміст сторінки "Про нас"'
