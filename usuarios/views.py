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
from django.utils.hashcompat import sha_constructor
# import code for encoding urls and generating md5 hashes --  GRAVATAR
import urllib, hashlib, random

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def sendEmailTest():
    username="Edwin Mesa"
    plaintext = get_template('usuarios/emailtest.txt')
    htmly     = get_template('usuarios/emailtest.html')
    d = Context({ 'username': username })
    subject, from_email, to = 'hello', 'Actarium <no-reply@daiech.com>', 'emesa@daiech.com'
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    

def nuevo_usuario(request):
    try:
        sendEmailTest()
    except:
        print "Error sending email"
    if request.method == "POST":
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            email_list = []
            email_user = formulario.cleaned_data['email']
            name_newuser = formulario.cleaned_data['username']
            salt = sha_constructor(str(random.random())).hexdigest()[:5]
            activation_key = sha_constructor(salt+email_user).hexdigest()            
            new_user = formulario.save()
            new_user.is_active = False
            new_user.save()
            from models import activation_keys
            activation_keys(id_user=new_user, email=email_user, activation_key= activation_key).save()
            
            email_list.append(str(email_user) + ",")
            try:
                title = "Bienvenido a DiaryCodes"
                contenido = "<strong>"+str(name_newuser)+"</strong> <br ><br> Te damos la bienvenida a DiaryCodes, solo falta un paso para activar tu cuenta. <br > Ingresa al siguiente link para activar tu cuenta: <a href='http://www.diarycodes.daiech.com/usuarios/activate/"+activation_key+"' >http://diarycodes.daiech.com/usuarios/activate/"+activation_key+"</a>"
#                print contenido
                sendEmail(email_list, title, contenido)
            except Exception, e:
                print "Exception mail: %s" % e
            return HttpResponseRedirect('/usuarios/ingresar',{},context_instance=RequestContext(request))
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


def activate_account(request,activation_key):
    if  not(activate_account_now(request,activation_key)== False):
#        print "La cuenta ha sido activada satisfactoriamente correo: "
        return render_to_response('usuarios/account_actived.html',{},context_instance = RequestContext(request))
    else:
#        print "La cuenta no se ha activado."
        return render_to_response('usuarios/invalid_link.html',{},context_instance = RequestContext(request))
    
    
def activate_account_now(request, activation_key):
    from models import activation_keys
    from django.contrib.auth.models import User
    try:
        activation_obj = activation_keys.objects.get(activation_key = activation_key)
    except  Exception, e:
        return False
#    print activation_obj
    if not(activation_obj.is_expired):
        user = User.objects.get(id=activation_obj.id_user.pk)
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        activation_obj.is_expired = True
        activation_obj.save()
        return True
    else: 
        return False

