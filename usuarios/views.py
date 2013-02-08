from django.shortcuts import render_to_response
#from django.contrib.auth.models import User
from usuarios.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.template import RequestContext #para hacer funcionar {% csrf_token %}

#Django Auth
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

# import code for encoding urls and generating md5 hashes --  GRAVATAR
import urllib, hashlib

def nuevo_usuario(request):
    if request.method == "POST":
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            email_list = []
#                for relation in relations:
                    #print "Nombre %s Correo %s, fecha %s"%(relation.id_user.username,relation.id_user.email,  str(datetime.datetime.strftime(make_naive(df['date_reunion'], get_default_timezone()), "%Y-%m-%d %I:%M %p")))
            email_user = formulario.cleaned_data['email']
            name_user = formulario.cleaned_data['username']  
            email_list.append(str(email_user) + ",")
            try:
                title = "Haz creado una nueva cuenta en Actarium"
                contenido = "Nombre de usuario: <strong>"+str(name_user)+"</strong>"
                sendEmail(email_list, title, contenido)
            except Exception, e:
                print "Exception mail: %s" % e
#            formulario.save()
            return HttpResponseRedirect('/usuarios/ingresar')
    else:
        formulario = RegisterForm()
    return render_to_response('usuarios/nuevo_usuario.html',{'formulario': formulario}, context_instance=RequestContext(request))
 
def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/usuarios/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)     
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)  
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/usuarios/privado')
                else:
                    return render_to_response('usuarios/noactivo.html', context_instance = RequestContext(request))
            else:
                return render_to_response('usuarios/nousuario.html', context_instance = RequestContext(request))
    else:
        formulario = AuthenticationForm()   
    return render_to_response('usuarios/ingresar.html',{'formulario':formulario}, context_instance = RequestContext(request))
                
                
@login_required(login_url='/usuarios/ingresar')
def privado(request):
    usuario = request.user
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
   
    return render_to_response('usuarios/privado.html',{'usuario':usuario, 'gravatar_url': gravatar_url}, context_instance = RequestContext(request))                    
                
                
@login_required(login_url='/usuarios/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def sendEmail(mail_to, titulo, contenido):
    contenido = contenido + "\n" + "<br><br><p style='color:gray'>Mensaje enviado por <a style='color:gray' href='http://daiech.com'>Daiech</a>. <br><br> Escribenos en twitter <a href='http://twitter.com/Actarium'>@Actarium</a> - <a href='http://twitter.com/Daiech'>@Daiech</a></p><br><br>"
    try:
        correo = EmailMessage(titulo, contenido, 'Actarium <no-reply@daiech.com>', mail_to)
        correo.content_subtype = "html"
        correo.send()
    except Exception, e:
        print e

