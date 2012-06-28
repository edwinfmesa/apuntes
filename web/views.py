from django.shortcuts import render_to_response

#funcion basica que recibe una solicitud y carga un html
def home(request):
    return render_to_response('web/home.html', None)

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