from app.models import Entrega, Fruta, Item, Pagamento, Verdura
from rest_framework import serializers


class VerduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verdura
        fields = "__all__"


class FrutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruta
        fields = "__all__"


class PagamentoSerializer(serializers.ModelSerializer):
    valor_total = serializers.DecimalField(
        max_digits=5, decimal_places=2, read_only=True
    )

    class Meta:
        model = Pagamento
        fields = "__all__"


class EntregaSerializer(serializers.ModelSerializer):
    metodo_pagamento = serializers.CharField(
        source="pagamento.metodo_pagamento", read_only=True
    )
    valor_total = serializers.DecimalField(
        source="pagamento.valor_total",
        max_digits=5,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Entrega
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"
