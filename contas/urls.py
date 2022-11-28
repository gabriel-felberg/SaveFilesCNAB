from contas import views
from django.urls import path

urlpatterns = [
    path("inicio/", views.inicio),
    path("uploadFile/", views.UploadedFileViews.as_view(), name="processando_form"),
    path("ShowData/", views.ShowResult),
    path("dados/", views.GetDataViews.as_view()),
]
