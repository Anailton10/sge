from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics

from categories.forms import CategoryForm
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = 'categories.view_category'

    def get_queryset(self):
        queryste = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryste = queryste.filter(name__icontains=name)

        return queryste


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    permission_required = 'categories.add_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):

    model = Category
    template_name = 'category_detail.html'
    permission_required = 'categories.view_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):

    model = Category
    template_name = 'category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    permission_required = 'categories.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):

    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category:list')
    permission_required = 'categories.delete_category'


class SupplierCreateListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
