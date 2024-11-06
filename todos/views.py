from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Categoria

class ProdutoListView(ListView):
    model = Produto
    template_name = 'todos/produto_list.html'
    context_object_name = 'produto_list'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome','descricao','preco','categoria']
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','descricao','preco','categoria']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')


# Categoria Views
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'todos/categoria_list.html'
    context_object_name = 'categoria_list'
    
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome','descricao']
    success_url = reverse_lazy('produto_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome','descricao']
    success_url = reverse_lazy('produto_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('produto_list')