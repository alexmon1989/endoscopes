from django.db.models import Prefetch, QuerySet

from .models import Category, CategoryImage, CategoryProperty


def category_get_all_items_enabled_qs() -> QuerySet[Category]:
    return Category.objects.enabled().order_by(
        'weight'
    ).prefetch_related(
        Prefetch(
            'categoryimage_set',
            queryset=CategoryImage.objects.order_by('weight')
        ),
        Prefetch(
            'categoryproperty_set',
            queryset=CategoryProperty.objects.order_by('weight')
        )
    )


def category_get_by_slug(slug: str) -> Category | None:
    category = Category.objects.filter(slug=slug).first()
    return category
