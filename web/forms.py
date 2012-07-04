from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User


class Apuntes(forms.Form):
    Email = forms.EmailField(widget = forms.TextInput())
    Titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea(attrs = {'cols':80,'rows': 15}))
    

