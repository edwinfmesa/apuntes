from django.db import models

# Create your models here.
class generales(models.Model):
    titulo = models.CharField(max_length = 40, verbose_name="Titulo")
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    hola ="hola mundo" 
    
    def __unicode__(self):
        return "%s "%(self.titulo)
    
class apuntes(models.Model):
    titulo = models.CharField(max_length = 40, verbose_name="Titulo")
    fecha = models.DateTimeField()
    texto = models.TextField(blank = True)
    
    def __unicode__(self):
        return "%s "%(self.titulo)
    
#    class Media:
#        js = ('/satic/tinyemc/jscripts/tiny_mce/tiny_mce.js',
##             '/static/js/admin.js'
#             )
