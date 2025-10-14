from django.db import models
from .baseModel import BaseModel

class CarrinhoProduto(BaseModel):
    carrinho = models.ForeignKey(
        'CarrinhoDeCompras',
        on_delete=models.CASCADE
    )
    produto = models.ForeignKey(
        'Produto',
        on_delete=models.CASCADE
    )
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.produto.preco
        super().save(*args, **kwargs)