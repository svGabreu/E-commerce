#from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Produto, Foto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class admListView(ListView):
    model = Categoria, Produto, Foto
    success_url = reverse_lazy("adm_list")


class admCreateView(CreateView):
    model = Categoria, Produto, Foto
    fields=["nome","descricao","preco","url"]
    success_url = reverse_lazy("adm_list")
    
class admUpdateView(UpdateView):
    model = Categoria, Produto, Foto
    fields=["nome","descricao","preco","url"]
    success_url = reverse_lazy("adm_list")

class admDeleteView(DeleteView):
    model = Categoria, Produto, Foto
    fields=["nome","descricao","preco","url"]
    success_url = reverse_lazy("adm_list")


def index(request):
    adm = Categoria, Produto, Foto.objects.all()
    return reverse_lazy(request, "adm/index.html",{"adm":adm})
