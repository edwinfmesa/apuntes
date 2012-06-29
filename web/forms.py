from django import forms

class Apuntes(forms.Form):
    Email = forms.EmailField(widget = forms.TextInput())
    Titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea())