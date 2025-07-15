from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import ContactsSettings
from .forms import ContactsForm


class ContactsPageView(TemplateView):
    """Відображає сторінку "Оплата та доставка"."""
    template_name = 'contacts/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsPageView, self).get_context_data(**kwargs)
        context['page'] = ContactsSettings.objects.first()
        if not context['page']:
            raise Http404("ContactsSettings does not exist.")

        return context


@require_POST
@csrf_exempt
def send_message(request):
    form = ContactsForm(request.POST)
    if form.is_valid():
        form.send_to_telegram()
        return HttpResponse('{:success:}')
    return HttpResponse('{:err:required:}')
