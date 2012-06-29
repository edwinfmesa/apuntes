from django.shortcuts import render_to_response
from web.models import generales, apuntes
from web.forms import Apuntes
from django.template import RequestContext #para hacer funcionar {% csrf_token %}
import datetime

#funcion basica que recibe una solicitud y carga un html
def home(request):
    p = generales.objects.order_by("-fecha")
    q = apuntes.objects.order_by("-fecha")
    #formularios
    info_enviado = False #si se envia el formaulario
#    email = ""
#    titulo = ""
#    texto = ""
    df = ""
    query = ""
    if request.method == "POST":
        form = Apuntes(request.POST)
        if form.is_valid():
            info_enviado = True
            df = {
                 'email': form.cleaned_data['Email'],
                'titulo': form.cleaned_data['Titulo'],
                'texto': form.cleaned_data['texto'],
                'info_enviado': info_enviado
            }
            query = apuntes(titulo= df['titulo'], fecha = datetime.datetime.now() , texto = df['texto']+' email: '+df['email'], )
            query.save()
    else:
        df = {}
        form = Apuntes()
    ctx = {'datos':  p, "apuntes": q, 'form':form}
    ctx.update(df)
    return render_to_response('web/home.html', ctx ,
                              context_instance = RequestContext(request)) #RequestContext #para hacer funcionar {% csrf_token %}

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