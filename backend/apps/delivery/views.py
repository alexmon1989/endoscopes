from django.http import Http404
from django.views.generic import TemplateView

from .models import DeliveryPage


class DeliveryPageView(TemplateView):
    """Відображає сторінку "Оплата та доставка"."""
    template_name = 'delivery/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(DeliveryPageView, self).get_context_data(**kwargs)
        context['page'] = DeliveryPage.objects.first()
        if not context['page']:
            raise Http404("DeliveryPage does not exist.")

        return context
