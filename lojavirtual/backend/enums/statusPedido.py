from django.utils.translation import gettext_lazy as _
from django.db import models

class StatusPedido(models.TextChoices):
    AGUARDANDOPAGAMENTO = "Aguardando pagamento", _("Aguardando pagamento")
    PAGO = "Pago", _("Pago")
    EMROTA = "Em rota", _("Em rota")
    ENTREGUE = "Entregue", _("Entregue")