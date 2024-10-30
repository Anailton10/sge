from django import forms

from brands.models import Brand


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['name', 'description']
        widgets = {  # Mapeia e personalisa os campos com a classe do bootstrap
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # em rows está definindo a quantidade inical de linhas no campo
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        #  Modificando o nome dos campos
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }
