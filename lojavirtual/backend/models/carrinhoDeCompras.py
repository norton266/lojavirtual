from .baseModel import BaseModel
from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .produto import Produto
from .carrinhoProduto import CarrinhoProduto

class CarrinhoDeCompras(BaseModel):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carrinhoDeCompras')
    criado_em= models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now=True)
    ativo= models.BooleanField(default=True)

    produtos = models.ManyToManyField(Produto, through=CarrinhoProduto,
                                       related_name='carrinhos')


    def __str__(self):
        return f"Carrinho {self.id} de {self.usuario.nome}"
    