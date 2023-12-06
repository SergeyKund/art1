from decimal import Decimal

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views import View

from apps.brand.models import Brand
from apps.product.forms import SearchForm


class BrandView(View):
    template_name = 'brands.html'

    def get(self, request):
        form = SearchForm()

        brands = Brand.objects.all()

        context = {
            'brands': brands,
            'form': form,
        }
        response = render(request, self.template_name, context=context)
        return response


def product_by_id(request, brand_id=None, *args, **kwargs):
    if not (brands := Brand.objects.filter(id=brand_id)):
        raise Http404("Brand does not exist")

    return render(request, 'brands.html', context={'brand': brands.last()})




# Create your views here.
