from .baseModel import BaseModel
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from ..enums import FormaDePagamento

class Pagamento(BaseModel):
    pedido = models.ForeignKey(
        'Pedido',
        on_delete= models.CASCADE,
        related_name= 'pagamentos'
    )
    dataPagamento = models.DateTimeField()
    formaDePagamento = models.CharField(
        choices= FormaDePagamento.choices,
        default= FormaDePagamento.PIX
    )
    valor = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )