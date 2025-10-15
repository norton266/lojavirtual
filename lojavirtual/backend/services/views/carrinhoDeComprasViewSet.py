from rest_framework.viewsets import ModelViewSet
from ..serializers.carrinhoDeComprasSerializer import CarrinhoDeComprasSerializer
from lojavirtual.backend.models.carrinhoDeCompras import CarrinhoDeCompras


class CarrinhoDeComprasViewSet(ModelViewSet):
    queryset = CarrinhoDeCompras.objects.all()
    serializer_class = CarrinhoDeComprasSerializer
