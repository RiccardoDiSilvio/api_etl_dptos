from django.urls import path

from . import views

urlpatterns = [
    path('departamento', views.transformer, name='index'),
]