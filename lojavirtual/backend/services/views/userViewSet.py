from rest_framework.viewsets import ModelViewSet
from ..serializers.userSerializer import UserSerializer
from lojavirtual.backend.models.user import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
