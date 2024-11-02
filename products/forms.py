from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'catogory', 'brand', 'description',
                  'serie_number', 'cost_price', 'selling_price',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'catogory': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serie_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),

        }

        #  Modificando o nome dos campos
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'title': 'Titulo',
            'catogory': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serie_number': 'Numero de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
        }
