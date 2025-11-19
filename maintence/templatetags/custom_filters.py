from django import template

register = template.Library()

@register.filter
def split(value, key):
    """
    Retorna uma lista de strings após dividir o valor pela chave.
    Uso: {{ value|split:"," }}
    """
    return value.split(key)
