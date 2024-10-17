from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Adm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class admListView(ListView):
    model = Adm

class admCreateView(CreateView):
    model = Adm
    fields=["title","deadline"]
    success_url = reverse_lazy("")
    
class admUpdateView(UpdateView):
    model = Adm

class admDeleteView(DeleteView):
    model = Adm


def index(request):
    return render(request, "adm/index.html")
