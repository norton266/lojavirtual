from rest_framework.viewsets import ModelViewSet
from ..serializers.pagamentoSerializer import PagamentoSerializer
from lojavirtual.backend.models.pagamento import Pagamento


class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
