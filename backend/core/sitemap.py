from django.contrib import sitemaps
from django.urls import reverse
from apps.catalog.services import category_get_all_items_enabled_qs


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return ['home', 'about', 'delivery', 'catalog', 'contacts']

    def location(self, item):
        return reverse(item)


class CategoriesSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return category_get_all_items_enabled_qs()

    def lastmod(self, obj):
        return obj.updated_at
