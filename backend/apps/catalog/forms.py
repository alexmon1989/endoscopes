import requests
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from apps.contacts.services import contacts_get_telegram_chat_id
from .models import Category, CategoryProperty
from .services import category_get_by_slug


class CategoryModelForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()
        widgets = {
            'price': forms.Textarea(attrs={'rows': 2, 'cols': 33})
        }


class CategoryPropertyModelForm(forms.ModelForm):

    class Meta:
        model = CategoryProperty
        exclude = ()
        widgets = {
            'value': forms.Textarea(attrs={'rows': 1, 'cols': 33})
        }


class OrderForm(forms.Form):
    action = forms.CharField(max_length=19)
    norobot = forms.CharField(max_length=100, required=False)
    category_slug = forms.CharField(max_length=100)
    contact_name = forms.CharField(max_length=100)
    contact_phone = forms.CharField(max_length=100)
    contact_message = forms.CharField(max_length=1024)

    def clean_action(self):
        value = self.cleaned_data.get('action')
        if value != 'order_submit':
            raise ValidationError("Недопустимое значение для action.")
        return value

    def clean_norobot(self):
        value = self.cleaned_data.get('norobot')
        if value:
            raise ValidationError("Поле norobot должно быть пустым.")
        return value

    def clean_category_slug(self):
        value = self.cleaned_data.get('category_slug')
        if not category_get_by_slug(value):
            raise ValidationError("Поле category_slug содержит неверное значение.")
        return value

    def send_to_telegram(self):
        token = settings.TELEGRAM_TOKEN
        chat_id = contacts_get_telegram_chat_id()
        if chat_id:
            category = category_get_by_slug(self.cleaned_data['category_slug'])
            text = (
                f"<b>Замовлення</b>\n\n"
                f"Категорія: {category.title}\n"
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
