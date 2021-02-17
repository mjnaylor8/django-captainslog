
'''
templatetags module
'''
import os
from django import template
from django.utils.safestring import mark_safe
from django.conf import settings
from django.urls import reverse
register = template.Library()

@register.simple_tag(takes_context=True)
def go_to_url(context, view_name, *args, **kwargs):
    fullurl = context['request'].build_absolute_uri(
        reverse(view_name, args=args, kwargs=kwargs))
    allels = ("window.location=", "'", fullurl, "'; return false;")
    returncmd = ''.join(allels)
    return mark_safe(returncmd)

# def absurl(context, object):
#     return context['request'].build_absolute_uri(object.get_absolute_url())    