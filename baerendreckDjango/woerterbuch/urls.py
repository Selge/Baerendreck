from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
path('buchstabe/', views.buchstabe_liste)
]
