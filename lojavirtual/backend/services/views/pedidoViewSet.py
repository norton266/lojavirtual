from rest_framework.viewsets import ModelViewSet
from ..serializers.pedidoSerializer import PedidoSerializer
from lojavirtual.backend.models.pedido import Pedido


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
