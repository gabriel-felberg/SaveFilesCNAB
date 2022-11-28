from ..models import Conta
from django.test import TestCase


class test_model_contas(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.file_data = {
            "Tipo": 3,
            "Data": "2019-03-01",
            "Valor": 1420,
            "CPF": "962.067.601-74",
            "Cartão": "753****3153",
            "Hora": "15:34:53",
            "DonoDaLoja": "JOÃO MACEDO",
            "NomeLoja": "BAR DO JOÃO",
        }

        cls.file = Conta.objects.create(**cls.file_data)

    def test_cpf_max_length(self):
        """Tem como função verificar o tamanho do campo CPF"""
        max_length = Conta._meta.get_field("CPF").max_length
        self.assertEqual(max_length, 14)

    def test_Cartão_max_length(self):
        """Tem como função verificar o tamanho do campo Cartão"""
        max_length = Conta._meta.get_field("Cartão").max_length
        self.assertEqual(max_length, 12)

    def test_DonoDaLoja_max_length(self):
        """Tem como função verificar o tamanho do campo DonoDaLoja"""
        max_length = Conta._meta.get_field("DonoDaLoja").max_length
        self.assertEqual(max_length, 50)

    def test_NomeLoja_max_length(self):
        """Tem como função verificar o tamanho do campo NomeLoja"""
        max_length = Conta._meta.get_field("NomeLoja").max_length
        self.assertEqual(max_length, 50)
