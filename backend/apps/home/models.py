from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from core.abstract_models import SeoModel, TimeStampedModel


class HomePage(SeoModel, TimeStampedModel):
    text_1 = RichTextField('Текст 1', blank=True)
    description = RichTextUploadingField('Опис', blank=True)

    def __str__(self):
        return 'Домашня сторінка'

    class Meta:
        verbose_name = 'Зміст сторінки'
        verbose_name_plural = 'Зміст сторінки'
