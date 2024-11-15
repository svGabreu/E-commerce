# Generated by Django 5.1.3 on 2024-11-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('preco', models.BigIntegerField(verbose_name='Preço')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
        ),
    ]
