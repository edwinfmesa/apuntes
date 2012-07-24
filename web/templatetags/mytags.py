from django import template
from django.template.defaultfilters import stringfilter
import os


register = template.Library()


@register.filter(name='basename')
@stringfilter
def basename(value):
    return os.path.basename(value)


















#import urllib, hashlib
#from django import template
#
#
#
#register = template.Library()
#
#@register.inclusion_tag('templatetags/gravatar.html')
#def show_gravatar(email, size=48):
#    default = "http://www.mysite.com/media/images/no-avatar.gif"
#
#    url = "http://www.gravatar.com/avatar.php?"
#    url += urllib.urlencode({
#        'gravatar_id': hashlib.md5(email).hexdigest(),
#        'default': default,
#        'size': str(size)
#    })
#
#    return {'gravatar': {'url': url, 'size': size}}