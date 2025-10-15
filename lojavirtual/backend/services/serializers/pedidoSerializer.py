from rest_framework import serializers
from lojavirtual.backend.models.pedido import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'