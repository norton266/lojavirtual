from .baseModel import BaseModel
from .user import User
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator

class Endereco(BaseModel):
    user = models.ForeignKey(
        'User',
        on_delete= models.CASCADE,
        related_name= 'enderecos'
    )
    rua = models.CharField(
        validators=[MaxLengthValidator(100), MinLengthValidator(4)],
        blank= False, null = False
    )
    numero = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(1)],
        blank = False, null = False
    )
    cidade = models.CharField(
        validators=[MaxLengthValidator(100), MinLengthValidator(3)],
        blank = False, null = False
    )
    estado = models.CharField(
        validators=[MaxLengthValidator(2), MinLengthValidator(2)],
        blank = False, null = False
    )
    cep = models.CharField(
        validators=[MaxLengthValidator(8), MinLengthValidator(8)],
        blank = False, null = False
    )