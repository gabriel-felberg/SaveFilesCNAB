from contas import views
from django.urls import path

urlpatterns = [
    path("start/", views.start),
    path("uploadFile/", views.UploadedFileViews.as_view(), name="processando_form"),
    path("ShowData/", views.ShowResult),
    path("dados/", views.GetDataViews.as_view()),
]
