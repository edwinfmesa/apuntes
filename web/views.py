from django.shortcuts import render_to_response
from web.models import Generales, Apuntes
#from django.contrib.auth.models import User
from web.forms import ApuntesForm  #, RegisterForm
from django.template import RequestContext #para hacer funcionar {% csrf_token %}

from django.contrib.auth.decorators import login_required # privacidad de formulario
import datetime


#Configuaracion para enviar correo
from django.core.mail import EmailMultiAlternatives  #Enviamos HTML
#from django.core.mail import send_mail


#funcion basica que recibe una solicitud y carga un html
def home(request):
    q = Generales.objects.order_by("-fecha")
    p = Apuntes.objects.order_by("-fecha")
    
    ctx = {'datos':  p, "apuntes": q}
#    ctx.update(df)
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

def apunte(request):
    q = Apuntes.objects.order_by("-fecha")
    ctx = {"apuntes": q}
    return render_to_response('web/apuntes.html', ctx , context_instance = RequestContext(request))

def apuntes2(request, slug, pk):
    q = Apuntes.objects.get(slug=slug, id=pk)
    ctx = {"apunte": q}
    return render_to_response('web/apunte.html', ctx, context_instance = RequestContext(request))


@login_required(login_url='/usuarios/ingresar')
def formulario(request):
        #formularios
    info_enviado = False #si se envia el formaulario
    df = {}
    query = ""
    if request.method == "POST":
        form = ApuntesForm(request.POST)
        if form.is_valid():
            info_enviado = True
            df = {
#                 'email': form.cleaned_data['Email'],
                'titulo': form.cleaned_data['Titulo'],
                'texto': form.cleaned_data['Texto'],
                'info_enviado': info_enviado
            }
            query = Apuntes(titulo= df['titulo'], fecha = datetime.datetime.now() , texto = df['texto'], user = request.user ) #+' email: '+df['email']
            query.save()
            
            #configuracion para enviar correo 
            to_admin = 'edwinfmesa@gmail.com'
            html_content = 'Se ha agregado un nuevo apunte: <br><br> %s <br><br><br>Desde: %s'#%(df['texto'],df['email'])
            msg = EmailMultiAlternatives('[Apuntes] %s'%(df['titulo']), html_content, 'admin@apuntes.sintramunicipio.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html') #deffinimos el ccontenido como HTML
#            msg.send() #Enviamos el correo
#            send_mail('Subject here', 'Here is the message.', 'edwinfmesa@gmail.com',['edwinfmesa@hotmail.com'], fail_silently=False)
    else:
        df = {}
        form = ApuntesForm()
    df.update({'formulario': form})
    return render_to_response('web/formulario.html', df, context_instance = RequestContext(request))





                