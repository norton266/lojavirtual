from .baseModel import BaseModel
from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from ..enums import FormaDePagamento
from ..enums import StatusPedido

class Pedido(BaseModel):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pedido')
    carrinho = models.ForeignKey(
        'CarrinhoDeCompras', on_delete=models.CASCADE
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    statusPedido = models.CharField(
        choices=StatusPedido.choices,
        default=StatusPedido.AGUARDANDOPAGAMENTO
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento do Pedido #{self.id}"