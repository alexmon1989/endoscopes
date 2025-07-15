from django.contrib import admin
from django.contrib.admin import TabularInline
from singlemodeladmin import SingleModelAdmin

from .forms import CategoryModelForm, CategoryPropertyModelForm
from .models import Category, CategoryImage, CategoryProperty, CatalogPage


class CategoryImageInline(TabularInline):
    model = CategoryImage
    ordering = ('weight', 'pk',)


class CategoryPropertyInline(TabularInline):
    model = CategoryProperty
    form = CategoryPropertyModelForm
    ordering = ('weight', 'pk',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'enabled', 'created_at', 'updated_at')
    list_filter = ('title',)
    list_editable = ('weight', 'enabled')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        CategoryImageInline,
        CategoryPropertyInline,
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "enabled",
                    "title",
                    "slug",
                    "price",
                    "description",
                    "weight",
                ],
            },
        ),
        (
            "SEO-налаштування",
            {
                "classes": ["collapse"],
                "fields": [
                    "meta_h1",
                    "meta_title",
                    "meta_keywords",
                    "meta_description",
                ],
            },
        ),
    ]
    form = CategoryModelForm


class CatalogPageAdmin(SingleModelAdmin):
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


admin.site.register(CatalogPage, CatalogPageAdmin)
