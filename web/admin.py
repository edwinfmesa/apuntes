from django.contrib import admin
from web.models import generales, apuntes
from django.conf import settings

class ApuntesAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('titulo', )}
#    ordering = ('-fecha', )

    # agregar editor de texto
    class Media:
        js = ('%stiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%sjs/textareas.js' % settings.STATIC_URL
        )

#        css = {
#            'all': ('css/admin.css', )
#        }


#registramos la tabla generales
admin.site.register(generales)
admin.site.register(apuntes, ApuntesAdmin)

