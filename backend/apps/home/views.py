from django.views.generic.base import TemplateView
from django.http import Http404

from apps.catalog.services import category_get_all_items_enabled_qs
from .models import HomePage


class HomeView(TemplateView):
    """Відображає головну сторінку."""
    template_name = 'home/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page'] = HomePage.objects.first()
        context['categories'] = category_get_all_items_enabled_qs()
        if not context['page']:
            raise Http404("HomePage does not exist.")

        return context
