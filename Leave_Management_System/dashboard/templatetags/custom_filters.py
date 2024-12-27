# dashboard/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def attr(obj, field_name):
    return getattr(obj, field_name, None)
