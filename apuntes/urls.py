from django.conf.urls import patterns, include, url
from django.contrib import admin
from usuarios.urls import usuarios_urls #agregar esta linea para incluir las URLS de usuarios
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home'),
    url(r'^enlaces/?$', 'web.views.enlaces2'),
    url(r'^enlaces/(?P<var>.+?)/?$', 'web.views.enlaces'),
    url(r'^instalaciones/', 'web.views.instalaciones'),
    url(r'^update/', 'github.views.update'),
    url(r'^formulario/', 'web.views.formulario' ),
    url(r'^apuntes/?$', 'web.views.apunte' ),
    url(r'^apuntes/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', 'web.views.apuntes2' ),
    #urls externas
    url('^usuarios/', include(usuarios_urls)), #incluye las urls para manejar los usuarios
    url(r'^admin/', include(admin.site.urls)), #incluye las urls de la aplicacion
)
