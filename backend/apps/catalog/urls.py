from django.urls import path

from .views import CatalogPageView, CategoryDetailView, CatalogOrderFormView, send_order


urlpatterns = [
    path('', CatalogPageView.as_view(), name="catalog"),
    path('get-order-form/<slug:slug>/', CatalogOrderFormView.as_view(), name="order_form"),
    path('order', send_order, name="send_order"),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name="category"),
]
