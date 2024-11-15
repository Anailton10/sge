from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics

from inflows.forms import InflowForm
from inflows.models import Inflow
from inflows.serializers import InflowSerializer


class InflowListaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):

    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryste = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryste = queryste.filter(product__title__icontains=product)

        return queryste


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):

    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow:list')
    permission_required = 'inflows.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):

    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
