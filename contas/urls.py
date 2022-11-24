from contas import views
from django.urls import path

urlpatterns = [
    path("inicio/", views.inicio),
    # path("processando_form/", views.processando_form, name="processando_form"),
    path("processando_form/", views.handle_uploaded_file, name="processando_form"),
]
