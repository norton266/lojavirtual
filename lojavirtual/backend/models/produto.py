from .baseModel import BaseModel
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

class Produto(BaseModel):
    nome = models.CharField(
        validators=[MaxLengthValidator(100), MinLengthValidator(2)]
    )
    preco = models.DecimalField(
        validators=[MaxValueValidator(1000000), MinValueValidator(0)],
        max_digits=10,
        decimal_places=2
    )
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome