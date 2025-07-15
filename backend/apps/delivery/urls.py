from django.urls import path

from .views import DeliveryPageView


urlpatterns = [
    path('', DeliveryPageView.as_view(), name="delivery"),
]
