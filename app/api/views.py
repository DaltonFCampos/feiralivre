from app.api.serializers import (EntregaSerializer, FrutaSerializer,
                                 ItemSerializer, PagamentoSerializer,
                                 VerduraSerializer)
from app.models import Entrega, Fruta, Item, Pagamento, Verdura
from rest_framework import status, viewsets
from rest_framework.response import Response

from .services import *


class VerduraViewSet(viewsets.ModelViewSet):
    queryset = Verdura.objects.all()
    serializer_class = VerduraSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        metrica = self.queryset.count() * 10 + 5
        return Response(
            {"message": "Verdura criada com sucesso!", "metrica": metrica}
        )


class FrutaViewSet(viewsets.ModelViewSet):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer


class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer


class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Pagamento excluído com sucesso!"})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        produto = serializer.validated_data['produto']
        quantidade = serializer.validated_data['quantidade']

        if Update_estoque(produto, quantidade):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Não há estoque suficiente para criar este item.", status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        resposta = Calcular_campo(response.data, "quantidade")
        return Response(resposta)
