from django.http import Http404
from django.views.generic import TemplateView

from .models import AboutPage


class AboutPageView(TemplateView):
    """Відображає сторінку "Оплата та доставка"."""
    template_name = 'about/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['page'] = AboutPage.objects.first()
        if not context['page']:
            raise Http404("AboutPage does not exist.")

        return context
