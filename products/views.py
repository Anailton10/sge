from django.urls import reverse_lazy
from django.views import generic

from brands.models import Brand
from categories.models import Category
from products.forms import ProductForm
from products.models import Product


class ProductListaView(generic.ListView):

    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        if category:
            queryset = queryset.filter(catogory__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context


class ProductCreateView(generic.CreateView):

    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductDetailView(generic.DetailView):

    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(generic.UpdateView):

    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductDeleteView(generic.DeleteView):

    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product:list')
