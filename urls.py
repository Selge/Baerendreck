from django.contrib import admin
from django.urls import path, include


# handler404 = 'woerterbuch.views.page_not_found'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woerterbuch.urls', namespace='worterbuch')),
    # path('about/', include('about.urls', namespace='about')),
]
