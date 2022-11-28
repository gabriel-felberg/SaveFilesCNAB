from rest_framework import serializers
from .models import Conta


class contaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = [
            "Tipo",
            "Data",
            "Valor",
            "CPF",
            "Cartão",
            "Hora",
            "DonoDaLoja",
            "NomeLoja",
        ]
