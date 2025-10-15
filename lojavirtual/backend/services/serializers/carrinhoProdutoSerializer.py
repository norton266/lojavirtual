from rest_framework import serializers
from lojavirtual.backend.models.carrinhoProduto import CarrinhoProduto


class CarrinhoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoProduto
        fields = '__all__'