from django import template
from my_app.models import Menu, Link

register = template.Library()

@register.simple_tag()
def get_menu():
    data = Menu.objects.filter(id=1).prefetch_related('link')
    print()
    return data