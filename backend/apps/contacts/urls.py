from django.urls import path

from .views import ContactsPageView, send_message


urlpatterns = [
    path('', ContactsPageView.as_view(), name="contacts"),
    path('send-message', send_message, name="send_message"),
]
