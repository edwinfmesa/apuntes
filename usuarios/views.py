from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from web.forms import Apuntes, RegisterForm
from django.http import HttpResponseRedirect
from django.template import RequestContext #para hacer funcionar {% csrf_token %}

#Django Auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def nuevo_usuario(request):
    if request.method == "POST":
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
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
    return render_to_response('usuarios/privado.html',{'usuario':usuario}, context_instance = RequestContext(request))                    
                
@login_required(login_url='/usuarios/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
