from django.shortcuts import render
from .models import Conta
from .serializer import ContaSerializer
from rest_framework import views, generics
from .utils.services import Handle_uploaded_file

# Create your views here.


class UploadedFileViews(views.APIView):
    def post(self, request: views.Request) -> views.Response:
        return Handle_uploaded_file(request.data)


class GetDataViews(generics.ListAPIView):

    serializer_class = ContaSerializer
    queryset = Conta.objects.all()


def start(request):
    form = ContaSerializer()
    return render(request, "contas/home.html", {"form": form})


def ShowResult(request):
    return render(request, "contas/result.html")
