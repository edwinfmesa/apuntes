from django.conf.urls import patterns, url

usuarios_urls = patterns('',
    (r'^usuario/nuevo', 'usuarios.views.nuevo_usuario'),
    (r'^ingresar', 'usuarios.views.ingresar'),
    (r'^privado', 'usuarios.views.privado'),
    (r'^cerrar', 'usuarios.views.cerrar'),
)
