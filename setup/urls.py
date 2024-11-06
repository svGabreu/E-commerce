# setup/urls.py
from django.contrib import admin
from django.urls import path
from todos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('create/', ProdutoCreateView.as_view(), name='produto_create'),
    path('update/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('delete/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),

    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),  # nova rota para deletar categoria
]
