from django.shortcuts import render_to_response
from web.models import generales, apuntes
#from django.contrib.auth.models import User
from web.forms import Apuntes  #, RegisterForm
from django.template import RequestContext #para hacer funcionar {% csrf_token %}
import datetime


#Configuaracion para enviar correo
from django.core.mail import EmailMultiAlternatives  #Enviamos HTML
#from django.core.mail import send_mail

# import code for encoding urls and generating md5 hashes --  GRAVATAR
import urllib, hashlib

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
            
            #configuracion para enviar correo 
            to_admin = 'edwinfmesa@gmail.com'
            html_content = 'Se ha agregado un nuevo apunte: <br><br> %s <br><br><br>Desde: %s'%(df['texto'],df['email'])
            msg = EmailMultiAlternatives('[Apuntes] %s'%(df['titulo']), html_content, 'admin@apuntes.sintramunicipio.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html') #deffinimos el ccontenido como HTML
#            msg.send() #Enviamos el correo
#            send_mail('Subject here', 'Here is the message.', 'edwinfmesa@gmail.com',['edwinfmesa@hotmail.com'], fail_silently=False)
            
    else:
        df = {}
        form = Apuntes()
    
    #GRAVATAR
    # Set your variables here
    if request.user.is_authenticated():
        email = request.user.email
        default = "http://cms.myspacecdn.com/cms/Music%20Vertical/Common/Images/default_small.jpg"
        size = 100
        
        # construct the url
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    else:
        gravatar_url = "/static/web/img/default.png"
    ctx = {'datos':  p, "apuntes": q, 'form':form, 'gravatar_url': gravatar_url}
    ctx.update(df)
    return render_to_response('web/home.html', ctx ,
                              context_instance = RequestContext(request)) #RequestContext #para hacer funcionar {% csrf_token %}

def enlaces(request,var):
#    if var != None:
#        contexto = {'nombre':var,'apellido': 'mesa salazar'}
#    else:
    contexto = {'nombre':var,'apellido': 'mesa salazar'}
    return render_to_response('web/enlaces.html', contexto ,context_instance = RequestContext(request) )

def enlaces2(request):
    return render_to_response('web/enlaces.html', None, context_instance = RequestContext(request))

def instalaciones(request):
    return render_to_response('web/instalaciones.html', None, context_instance = RequestContext(request))

               
        





                