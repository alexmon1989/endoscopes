from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from .managers import CategoryManager
from core.abstract_models import TimeStampedModel, SeoModel


class Category(TimeStampedModel, SeoModel):
    """Модель категорії."""
    enabled = models.BooleanField('Увімкнено', default=True, help_text='Чи відображати на веб-сайті дану категорію?')
    title = models.CharField('Назва', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
    )
    price = models.TextField(
        'Вартість',
        blank=True
    )
    description = RichTextUploadingField('Опис')
    weight = models.PositiveIntegerField(
        'Вага',
        default=1000,
        help_text='Чим більша вага, тим далі елемент буде у списку на сторінці'
    )

    objects = CategoryManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class CategoryImage(TimeStampedModel):
    """Модель зображення категорії."""
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        'Зображення',
        upload_to="uploads/%Y/%m/%d/",
        help_text='Зображення буде автоматично приведено до розміру 800*800 пікселей при виводі на сторінці категорії.'
    )
    weight = models.PositiveIntegerField(
        'Вага',
        default=1000,
        help_text='Чим більша вага, тим далі елемент буде у списку на сторінці'
    )

    class Meta:
        verbose_name = 'Зображення категорії'
        verbose_name_plural = 'Зображення категорії'


class CategoryProperty(TimeStampedModel):
    """Модель характеристики категорії."""
    category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE, default=None)
    key = models.CharField('Назва', max_length=255)
    value = models.TextField('Значення')
    weight = models.PositiveIntegerField(
        'Вага',
        default=1000,
        help_text='Чим більша вага, тим далі елемент буде у списку на сторінці'
    )

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Характеристика категорії'
        verbose_name_plural = 'Характеристики категорії'


class CatalogPage(SeoModel, TimeStampedModel):
    description = RichTextUploadingField('Опис', blank=True)

    def __str__(self):
        return 'Сторінка списку категорій'

    class Meta:
        verbose_name = 'Зміст сторінки списку категорій'
        verbose_name_plural = 'Зміст сторінки списку категорій'
