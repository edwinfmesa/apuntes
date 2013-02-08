from django.db import models
from django.template import defaultfilters
from django.contrib.auth.models import User

#class ActivationManager(models.Manager):
#    """
#    This class is responsible to manage the process of  account activation.
#    """
    
        
class activation_keys(models.Model):
    """
    Table necessary for create an user account, This serves to validate the email.
    """
    id_user = models.ForeignKey(User,  null=False, related_name='%(class)s_id_user')
    email = models.CharField(max_length=150, verbose_name="Email")
    activation_key = models.CharField(max_length=150, verbose_name = "Activation_key")
    date_generated = models.DateTimeField(auto_now=True)
    is_expired = models.BooleanField(default=False)
#    objects = ActivationManager()
    
    def __unicode__(self):
        return "%s "%(self.email)
    
    
        