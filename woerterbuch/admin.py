from django.contrib import admin
from .models import Wort, Dialekt, Buchstabe


admin.site.register(Buchstabe)
admin.site.register(Dialekt)
admin.site.register(Wort)
