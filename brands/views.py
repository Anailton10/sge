from django.urls import reverse_lazy
from django.views import generic

from brands.forms import BrandForm
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


class BrandCreateView(generic.CreateView):

    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand:list')


class BrandDetailView(generic.DetailView):

    model = Brand
    template_name = 'brand_datail.html'


class BrandUpdateView(generic.UpdateView):

    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand:list')


class BrandDeleteView(generic.DeleteView):

    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand:list')
