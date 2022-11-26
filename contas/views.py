from django.shortcuts import render
from .models import Conta
from .serializer import contaSerializer
from rest_framework import views, generics
from .utils.services import handle_uploaded_file

# Create your views here.


class UploadedFileViews(views.APIView):
    def post(self, request: views.Request) -> views.Response:
        return handle_uploaded_file(request.data)


class GetDataViews(generics.ListAPIView):

    serializer_class = contaSerializer
    queryset = Conta.objects.all()


def inicio(request):
    form = contaSerializer()
    return render(request, "contas/home.html", {"form": form})


def ShowResult(request):
    return render(request, "contas/result.html")
