from rest_framework import serializers
from lojavirtual.backend.models.carrinhoDeCompras import CarrinhoDeCompras


class CarrinhoDeComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoDeCompras
        fields = '__all__'