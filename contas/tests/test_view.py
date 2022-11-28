from rest_framework.test import APITestCase
from ..utils.services import test_Handle_uploaded_file
from ..models import Conta


class test_view_contas(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.file_upload = test_Handle_uploaded_file()
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

    def test_keys_of_CNAB(self):
        """Tem como função verificar todas as chaves já escritas"""
        expeted = [
            "Tipo",
            "Data",
            "Valor",
            "CPF",
            "Cartão",
            "Hora",
            "DonoDaLoja",
            "NomeLoja",
        ]
        result = []

        for key, value in self.file_upload[0].items():
            result.append(key)

        self.assertEqual(result, expeted, f"Era esperado as chaves: {expeted}")

    def test_get_conta(self):
        """Deve pegar todas as contas criadas"""
        conta_response = self.client.get("/api/dados/")
        self.assertEqual(len(conta_response.data), 1, "Deve conter apenas 1 de tamanho")
