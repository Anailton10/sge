from django.urls import reverse_lazy
from django.views import generic

from outflows.forms import OutflowForm
from outflows.models import Outflow


class OutflowListaView(generic.ListView):

    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryste = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryste = queryste.filter(product__title__icontains=product)

        return queryste


class OutflowCreateView(generic.CreateView):

    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow:list')


class OutflowDetailView(generic.DetailView):

    model = Outflow
    template_name = 'outflow_detail.html'
