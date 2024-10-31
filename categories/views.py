from django.urls import reverse_lazy
from django.views import generic

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListaView(generic.ListView):

    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryste = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryste = queryste.filter(name__icontains=name)

        return queryste


class CategoryCreateView(generic.CreateView):

    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')


class CategoryDetailView(generic.DetailView):

    model = Category
    template_name = 'category_detail.html'


class CategoryUpdateView(generic.UpdateView):

    model = Category
    template_name = 'category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')


class CategoryDeleteView(generic.DeleteView):

    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category:list')
