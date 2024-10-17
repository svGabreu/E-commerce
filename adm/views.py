from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Categoria, Produto, Foto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class admListView(ListView):
    model = Categoria, Produto, Foto

class admCreateView(CreateView):
    model = Categoria, Produto, Foto
    fields=["title","deadline"]
    success_url = reverse_lazy("")
    
class admUpdateView(UpdateView):
    model = Categoria, Produto, Foto

class admDeleteView(DeleteView):
    model = Categoria, Produto, Foto


def index(request):
    adm = Categoria, Produto, Foto.objects.all()
    return render(request, "adm/index.html",{"adm":adm})
