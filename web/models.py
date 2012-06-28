from django.db import models

# Create your models here.
class generales(models.Model):
    titulo = models.CharField(max_length = 20, verbose_name="Titulo")
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    hola ="hola mundo" 
    
    def __unicode__(self):
        return "%s "%(self.titulo)