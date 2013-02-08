from django.conf.urls import patterns, url

usuarios_urls = patterns('',
    (r'^usuario/nuevo', 'usuarios.views.nuevo_usuario'),
    (r'^activate/(?P<activation_key>[-\w]+)', 'usuarios.views.activate_account'),
    (r'^ingresar', 'usuarios.views.ingresar', ),
    (r'^privado', 'usuarios.views.privado'),
    (r'^cerrar', 'usuarios.views.cerrar'),
)
