from rest_framework.viewsets import ModelViewSet
from ..serializers.produtoSerializer import ProdutoSerializer
from lojavirtual.backend.models.produto import Produto


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
