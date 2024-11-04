from django.db.models.signals import post_save
from django.dispatch import receiver

from inflows.models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    # sender - o que avisa sobre o evento(nesse caso Inflow)
    # instance - os dados que o usuario vai mandar
    # created - se for "True" sinal que ta criando registro se for "False" está atualizando
    if created:
        if instance.quantity > 0:
            # pegando o produto que o usuario selecionou
            product = instance.product
            # pegando a quantidade atual do produto e adicionando a entrada
            product.quantity += instance.quantity
            # salvando a ação
            product.save()
