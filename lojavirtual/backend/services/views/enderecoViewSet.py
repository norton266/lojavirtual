from rest_framework.viewsets import ModelViewSet
from ..serializers.enderecoSerializer import EnderecoSerializer
from lojavirtual.backend.models.endereco import Endereco


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
