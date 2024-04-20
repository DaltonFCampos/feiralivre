from django.core.validators import MinValueValidator
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"


class Verdura(Produto):
    pass


class Fruta(Produto):
    pass


class Pagamento(models.Model):
    metodo_pagamento = models.CharField(max_length=50)

    @property
    def valor_total(self):
        total = 0

        for item in self.entrega.itens.all():
            total += item.calcular_subtotal

        return total

    def __str__(self):
        return f"{self.metodo_pagamento}"


class Item(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, null=False, blank=False
    )
    quantidade = models.IntegerField(validators=[MinValueValidator(0)])

    @property
    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto} - {self.quantidade}"


class Entrega(models.Model):
    nome_cliente = models.CharField(max_length=255)
    endereco_entrega = models.TextField()
    data_entrega = models.DateTimeField()
    pagamento = models.OneToOneField(
        "Pagamento", on_delete=models.CASCADE, related_name="entrega"
    )
    itens = models.ManyToManyField(Item, related_name="entregas")

    def __str__(self):
        return f"{self.nome_cliente} - {self.data_entrega}"
