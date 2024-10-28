from django.views import generic

from brands.models import Brand


class BrandListaView(generic.ListView):

    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryste = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryste = queryste.filter(name__icontains=name)

        return queryste
