from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This is gonna cut the value out of that string
    """
    return value.replace(arg, '')

# register.filter('cut', cut)