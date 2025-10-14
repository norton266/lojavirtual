from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class User(AbstractUser):
    nome = models.CharField(
        validators=[MaxLengthValidator(100), MinLengthValidator(5)],
        blank= False, null= False
    )
    cpf = models.CharField(
        validators=[MaxLengthValidator(11), MinLengthValidator(11)],
        blank = False, null= False
    )
    telefone = models.CharField(
        validators=[MaxLengthValidator(9),MinLengthValidator(8)]
    )
    
    def __str__(self):
        return f"{self.username}"