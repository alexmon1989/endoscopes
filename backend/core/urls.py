"""
URL configuration for endoscopes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemap import StaticViewSitemap, CategoriesSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "categories": CategoriesSitemap,
}


def health_check(request):
    return HttpResponse("OK")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.home.urls')),
    path("health/", health_check),
    path('about/', include('apps.about.urls')),
    path('delivery/', include('apps.delivery.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
