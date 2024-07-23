from django import template
from my_app.models import Menu, Link

register = template.Library()

@register.simple_tag()
def dra_menu():
    data = Menu.objects.filter(id=1).prefetch_related('link')
    return data

@register.inclusion_tag('my_app/list_menu.html')
def draw_menu(filter: str) -> dict:
    queryset = Menu.objects.get(name=filter).link.order_by('parent')
    return {'queryset': queryset, 'menu': filter}