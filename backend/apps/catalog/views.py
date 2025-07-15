from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.http import Http404, HttpResponse

from .forms import OrderForm
from .models import CatalogPage, Category
from .services import category_get_all_items_enabled_qs


class CatalogPageView(TemplateView):
    """Відображає сторінку списку категорій."""
    template_name = 'catalog/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogPageView, self).get_context_data(**kwargs)
        context['page'] = CatalogPage.objects.first()
        context['categories'] = category_get_all_items_enabled_qs()
        if not context['page']:
            raise Http404("CatalogPage does not exist.")

        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category/index.html'
    queryset = category_get_all_items_enabled_qs()


class CatalogOrderFormView(TemplateView):
    template_name = 'catalog/category/_partials/form.html'


@require_POST
@csrf_exempt
def send_order(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.send_to_telegram()
        return HttpResponse('{:success:}')
    print(form.errors)
    return HttpResponse('{:err:required:}')
