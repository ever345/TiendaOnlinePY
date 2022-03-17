from atexit import register
from django import template

register = template.Library()

@register.filter()
def quantify_product_format(quantify=1):
                                #operador terneario
    return '{} {}'.format(quantify, 'productos' if quantify > 1 else 'producto')

@register.filter()
def quantify_add_format(quantify):
    return '{} {}'.format(quantify_product_format(quantify),'agregados' if quantify > 1 else 'agregado')