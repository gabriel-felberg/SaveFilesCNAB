from datetime import datetime, timedelta
from django.shortcuts import redirect
from ..serializer import contaSerializer


def handle_uploaded_file(request):
    with open("file.txt", "wb+") as destination:
        for chunk in request["arquivo"].chunks():
            destination.write(chunk)

    with open("file.txt", encoding="utf-8") as destination:
        file = destination.readlines()
        json = []
        for line in file:
            obj = {
                "Tipo": line[0],
                "Data": f"{line[1:5]}-{line[6:7]}-{line[8]}",
                "Valor": int(int(line[10:20]) / 100),
                "CPF": f"{line[20:23]}.{line[23:26]}.{line[26:29]}-{line[29:31]}",
                "Cartão": f"{line[31:43]}",
                "Hora": time_zone_correct(
                    int(line[1:5]),
                    int(line[6:7]),
                    int(line[8]),
                    int(line[42:44]),
                    int(line[44:46]),
                    int(line[46:48]),
                ),
                "DonoDaLoja": f"{line[48:62]}",
                "NomeLoja": f"{line[62:-1]}",
            }
            json.append(obj)
            serializer = contaSerializer(data=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return redirect("/api/ShowData/")


def time_zone_correct(ano, mes, dia, hora, minuto, segundo):
    data_atual = datetime(
        year=ano, month=mes, day=dia, hour=hora, minute=minuto, second=segundo
    ) - timedelta(hours=3)
    return data_atual.strftime("%H:%M:%S")


def test_handle_uploaded_file():
    with open("file.txt", encoding="utf-8") as destination:
        file = destination.readlines()
        json = []
        for line in file:
            obj = {
                "Tipo": line[0],
                "Data": f"{line[1:5]}-{line[6:7]}-{line[8]}",
                "Valor": int(int(line[10:20]) / 100),
                "CPF": f"{line[20:23]}.{line[23:26]}.{line[26:29]}-{line[29:31]}",
                "Cartão": f"{line[31:43]}",
                "Hora": time_zone_correct(
                    int(line[1:5]),
                    int(line[6:7]),
                    int(line[8]),
                    int(line[42:44]),
                    int(line[44:46]),
                    int(line[46:48]),
                ),
                "DonoDaLoja": f"{line[48:62]}",
                "NomeLoja": f"{line[62:-1]}",
            }
            json.append(obj)
        return json
