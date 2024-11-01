from django import forms
from django.core.exceptions import ValidationError

from outflows.models import Outflow


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            #   Select pois ambos são FK
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        #  Modificando o nome dos campos
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponivel em estoque para o produto {product.title} é de {product.quantity} unidades'
            )
        return quantity
