from django.views import generic

from brands.models import Brand


class BrandListaView(generic.ListView):

    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
