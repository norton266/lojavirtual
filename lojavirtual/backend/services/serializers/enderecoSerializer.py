from rest_framework import serializers
from lojavirtual.backend.models.endereco import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'