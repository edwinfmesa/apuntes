from django.contrib import admin
from web.models import generales, apuntes

#registramos la tabla generales
admin.site.register(generales)
admin.site.register(apuntes)