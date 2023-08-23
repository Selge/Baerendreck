from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'woerterbuch.views.page_not_found'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woerterbuch.urls', namespace='worterbuch')),
    path('about/', include('about.urls', namespace='about')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
