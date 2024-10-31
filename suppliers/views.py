from django.urls import reverse_lazy
from django.views import generic

from suppliers.forms import SupplierForm
from suppliers.models import Supplier


class SupplierListaView(generic.ListView):

    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryste = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryste = queryste.filter(name__icontains=name)

        return queryste


class SupplierCreateView(generic.CreateView):

    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier:list')


class SupplierDetailView(generic.DetailView):

    model = Supplier
    template_name = 'supplier_datail.html'


class SupplierUpdateView(generic.UpdateView):

    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier:list')


class SupplierDeleteView(generic.DeleteView):

    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier:list')
