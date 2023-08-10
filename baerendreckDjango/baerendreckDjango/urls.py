from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include()),
    path('buchstabe/', views.buchstabe_liste),
    path('buchstabe/<slug:pk>/', views.buchstabe),
]
