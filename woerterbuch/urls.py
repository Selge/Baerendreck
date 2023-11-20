from django.urls import path

from . import views

app_name = 'woerterbuch'

urlpatterns = [
    path('', views.index),
    # path('buchstabe/', views.buchstabe_liste),
    # path('buchstabe/<slug:pk>/', views.buchstabe),
]
