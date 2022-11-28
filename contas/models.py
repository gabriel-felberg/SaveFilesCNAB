from django.db import models


class Conta(models.Model):
    Tipo = models.IntegerField()
    Data = models.DateField()
    Valor = models.IntegerField()
    CPF = models.CharField(max_length=14)
    Cartão = models.CharField(max_length=12)
    Hora = models.TimeField()
    DonoDaLoja = models.CharField(max_length=50)
    NomeLoja = models.CharField(max_length=50)
