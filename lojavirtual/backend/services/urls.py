from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.carrinhoDeComprasViewSet import CarrinhoDeComprasViewSet
from .views.carrinhoProdutoViewSet import CarrinhoProdutoViewSet
from .views.enderecoViewSet import EnderecoViewSet
from .views.pagamentoViewSet import PagamentoViewSet
from .views.pedidoViewSet import PedidoViewSet
from .views.produtoViewSet import ProdutoViewSet
from.views.userViewSet import UserViewSet

router = DefaultRouter()
router.register(r'carrinhoDeCompras', CarrinhoDeComprasViewSet, basename='carrinhoDeCompras')
router.register(r'carrinhoProduto', CarrinhoProdutoViewSet, basename='carrinhoProduto')
router.register(r'endereco', EnderecoViewSet, basename='endereco')
router.register(r'pagamento', PagamentoViewSet, basename='pagamento')
router.register(r'pedido', PedidoViewSet, basename='pedido')
router.register(r'produto', ProdutoViewSet, basename='produto')
router.register(r'user', UserViewSet, basename='user')

app_name='api'
urlpatterns = [
    path('', include(router.urls)),
]

