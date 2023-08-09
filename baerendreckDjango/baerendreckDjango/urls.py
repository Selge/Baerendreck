from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('buchstabe/', views.buchstabe_liste),
    path('buchstabe/')
]
