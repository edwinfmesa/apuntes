from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Apuntes(forms.Form):
    Email = forms.EmailField(widget = forms.TextInput())
    Titulo = forms.CharField(widget = forms.TextInput())
    texto = forms.CharField(widget = forms.Textarea(attrs = {'cols':80,'rows': 15}))
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "email", )
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
