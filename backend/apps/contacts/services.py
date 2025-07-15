from .models import ContactsSettings


def contacts_get_telegram_chat_id() -> int | None:
    contacts = ContactsSettings.objects.all().values('telegram_chat_id').first()
    if contacts and contacts['telegram_chat_id']:
        return contacts['telegram_chat_id']
    return None
