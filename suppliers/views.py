from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics

from suppliers.forms import SupplierForm
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class SupplierListaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):

    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        queryste = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryste = queryste.filter(name__icontains=name)

        return queryste


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):

    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier:list')
    permission_required = 'suppliers.add_supplier'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):

    model = Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):

    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier:list')
    permission_required = 'suppliers.change_supplier'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):

    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier:list')
    permission_required = 'suppliers.delete_supplier'


class SupplierCreateListAPIView(generics.RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
