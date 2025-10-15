from rest_framework.viewsets import ModelViewSet
from ..serializers.carrinhoProdutoSerializer import CarrinhoProdutoSerializer
from lojavirtual.backend.models.carrinhoProduto import CarrinhoProduto


class CarrinhoProdutoViewSet(ModelViewSet):
    queryset = CarrinhoProduto.objects.all()
    serializer_class = CarrinhoProdutoSerializer
