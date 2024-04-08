from django.db import models

class Verduras(models.Model):
    nmVdx = models.CharField(max_length=100)
    pXcVdX = models.DecimalField(max_digits=6, decimal_places=2)
    stkVxL = models.IntegerField()

class Frutas(models.Model):
    nmeFrt = models.CharField(max_length=100)
    prcFrt = models.DecimalField(max_digits=6, decimal_places=2)
    qntdDspnvl = models.IntegerField()

class Entrega(models.Model):
    nmClnt = models.CharField(max_length=255)
    endrNtrg = models.TextField()
    dtEntrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

class Pagamento(models.Model):
    mtPgto = models.CharField(max_length=50)
    vlrTotal = models.DecimalField(max_digits=8, decimal_places=2)

class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nmItm = models.CharField(max_length=100)
    qntdd = models.IntegerField()
    prcUnit = models.DecimalField(max_digits=6, decimal_places=2)
