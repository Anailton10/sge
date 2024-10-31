from django import forms

from inflows.models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            #   Select pois ambos são FK
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        #  Modificando o nome dos campos
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
