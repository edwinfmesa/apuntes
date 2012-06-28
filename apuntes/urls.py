from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home'),
    url(r'^enlaces/?$', 'web.views.enlaces2'),
    url(r'^enlaces/(?P<var>.+?)/?$', 'web.views.enlaces'),
    url(r'^instalaciones/', 'web.views.instalaciones'),
    url(r'^update/', 'github.views.update'),
    # url(r'^apuntes/', include('apuntes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), #incluye las urls de la aplicacion
)
