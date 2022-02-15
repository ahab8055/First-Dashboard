from django import template

register = template.Library()

@register.filter
def abs(value):
    value = -1 * value
    return value