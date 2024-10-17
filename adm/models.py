from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    preco = models.CharField(max_length=100, null=False, blank=False)

class Foto(models.Model):
    url = models.CharField(max_length=200, null=False, blank=False)
