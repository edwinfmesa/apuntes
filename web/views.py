from django.shortcuts import render_to_response
from web.models import generales, apuntes

#funcion basica que recibe una solicitud y carga un html
def home(request):
    p = generales.objects.order_by("fecha")
    q = apuntes.objects.order_by("fecha")
    return render_to_response('web/home.html', {'datos':  p, "apuntes": q})

def enlaces(request,var):
#    if var != None:
#        contexto = {'nombre':var,'apellido': 'mesa salazar'}
#    else:
    contexto = {'nombre':var,'apellido': 'mesa salazar'}
    return render_to_response('web/enlaces.html', contexto )

def enlaces2(request):
    return render_to_response('web/enlaces.html')

def instalaciones(request):
    return render_to_response('web/instalaciones.html', None)