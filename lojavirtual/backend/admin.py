from django.contrib import admin
from .models.user import User
from .models.carrinhoDeCompras import CarrinhoDeCompras
from .models.carrinhoProduto import CarrinhoProduto
from .models.endereco import Endereco
from .models.pagamento import Pagamento
from .models.pedido import Pedido
from .models.produto import Produto



# Inline para adicionar produtos ao carrinho
class CarrinhoProdutoInline(admin.TabularInline):
    model = CarrinhoProduto
    extra = 1  # número de linhas vazias para adicionar
    autocomplete_fields = ['produto']  # opcional: busca automática de produtos

# Admin personalizado para CarrinhoDeCompras
@admin.register(CarrinhoDeCompras)
class CarrinhoDeComprasAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'ativo', 'criado_em']
    inlines = [CarrinhoProdutoInline]

# Admin normal para os outros models
admin.site.register(User)
admin.site.register(Endereco)
admin.site.register(Pagamento)
admin.site.register(Pedido)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']  # <-- necessário para autocomplete_fields
