from rest_framework import serializers
from lojavirtual.backend.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'