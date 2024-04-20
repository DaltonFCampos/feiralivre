from rest_framework.response import Response


def Update_estoque(produto, quantidade):
    if produto.estoque < quantidade:
        return False
    produto.estoque -= quantidade
    produto.save()
    return True

def Calcular_campo(item, campo):
    item[campo] *= 2
    return item