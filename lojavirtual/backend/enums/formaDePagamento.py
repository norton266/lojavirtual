from django.utils.translation import gettext_lazy as _
from django.db import models

class FormaDePagamento(models.TextChoices):
    PIX = "Pix", _("Pix")
    CREDITO = "Crédito", _("Crédito")
    DEBITO = "Débito", _("Débito")