from django.urls import reverse_lazy
from django.views import generic

from inflows.forms import InflowForm
from inflows.models import Inflow


class InflowListaView(generic.ListView):

    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryste = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryste = queryste.filter(product__title__icontains=product)

        return queryste


class InflowCreateView(generic.CreateView):

    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow:list')


class InflowDetailView(generic.DetailView):

    model = Inflow
    template_name = 'inflow_detail.html'
