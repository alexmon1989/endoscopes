import requests

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from .services import contacts_get_telegram_chat_id


class ContactsForm(forms.Form):
    action = forms.CharField(max_length=19)
    norobot = forms.CharField(max_length=100, required=False)
    contact_name = forms.CharField(max_length=100)
    contact_phone = forms.CharField(max_length=100)
    contact_message = forms.CharField(max_length=1024)

    def clean_action(self):
        value = self.cleaned_data.get('action')
        if value != 'contact_form_submit':
            raise ValidationError("Недопустимое значение для action.")
        return value

    def clean_norobot(self):
        value = self.cleaned_data.get('norobot')
        if value:
            raise ValidationError("Поле norobot должно быть пустым.")
        return value

    def send_to_telegram(self):
        token = settings.TELEGRAM_TOKEN
        chat_id = contacts_get_telegram_chat_id()
        if chat_id:
            text = (
                f"<b>Повідомлення із форми контактів</b>\n\n"
                f"Ім'я: {self.cleaned_data['contact_name']}\n"
                f"Телефон: {self.cleaned_data['contact_phone']}\n"
                f"Повідомлення: {self.cleaned_data['contact_message']}"
            )

            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode': 'HTML',
            }

            response = requests.post(url, data=payload)
            response.raise_for_status()
