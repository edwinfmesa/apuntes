import urllib, hashlib
from django import template

register = template.Library()

@register.inclusion_tag('templatetags/gravatar.html')
def showgravatar(email, size=48):
    default = "http://cms.myspacecdn.com/cms/Music%20Vertical/Common/Images/default_small.jpg"

    url = "http://www.gravatar.com/avatar.php?"
    url += urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default': default,
        'size': str(size)
    })

    return {'gravatar': {'url': url, 'size': size}}


#import urllib, hashlib
#from django import template
#
#
#
#register = template.Library()
#
#@register.inclusion_tag('templatetags/gravatar.html')
#def showgravatar(email, size=48):
#    default = "http://cms.myspacecdn.com/cms/Music%20Vertical/Common/Images/default_small.jpg"
#
#    url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
#    url += urllib.urlencode({'d':default, 's':str(size)})
#    
#    return {'gravatar': {'url': url, 'size': size}}