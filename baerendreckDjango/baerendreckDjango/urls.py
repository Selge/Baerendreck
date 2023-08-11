from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woerterbuch.urls')),
    # ,
    # path('buchstabe/<slug:pk>/', views.buchstabe),
]
