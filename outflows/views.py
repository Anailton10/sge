from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app import metrics
from outflows.forms import OutflowForm
from outflows.models import Outflow


class OutflowListaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):

    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryste = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryste = queryste.filter(product__title__icontains=product)

        return queryste

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics
        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):

    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow:list')
    permission_required = 'outflows.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):

    model = Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'
