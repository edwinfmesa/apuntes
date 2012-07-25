from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User

# Create your models here.
class Generales(models.Model):
    titulo = models.CharField(max_length = 60, verbose_name="Titulo")
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    hola ="hola mundo" 
    
    def __unicode__(self):
        return "%s "%(self.titulo)
    
class Apuntes(models.Model):
    titulo = models.CharField(max_length = 60, verbose_name="Titulo")
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return "%s "%(self.titulo)
    
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo)
        super(Apuntes, self).save(*args, **kwargs)