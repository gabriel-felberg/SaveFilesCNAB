from django.shortcuts import render, HttpResponse
from .models import Conta
from .serializer import contaSerializer
from rest_framework.views import APIView, Response, Request, status

# Create your views here.


class ContasViews(APIView):
    def get(self, request: Request) -> Response:
        users = Conta.objects.all()
        # [lista_de_objetos_User].first_name
        serializer = contaSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        handle_uploaded_file(request.data)


def inicio(request):
    form = contaSerializer()
    return render(request, "contas/home.html", {"form": form})


def handle_uploaded_file(request):
    with open("file.txt", "wb+") as destination:
        for chunk in request.FILES["nome"].chunks():
            destination.write(chunk)

    with open("file.txt", encoding="utf-8") as destination:

        file = destination.readlines()

        json = []
        for line in file:
            obj = {
                "Tipo": line[0],
                "Data": f"{line[1:5]}-{line[6:7]}-{line[8]}",
                "Valor": line[10:20],
                "CPF": f"{line[20:23]}.{line[23:26]}.{line[26:29]}-{line[29:31]}",
                "Cartão": f"{line[31:43]}",
                "Hora": f"{line[42]+line[43]}:{line[44:46]}:{line[46:48]}",
                "DonoDaLoja": f"{line[48:62]}",
                "NomeLoja": f"{line[62:-1]}",
            }
            json.append(obj)
            serializer = contaSerializer(data=obj)
            serializer.is_valid(raise_exception=True)

            serializer.save()

    return HttpResponse(serializer.data)
