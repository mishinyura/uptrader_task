from django import template
from my_app.models import Menu

register = template.Library()

@register.inclusion_tag('my_app/list_menu.html')
def draw_menu(filter: str) -> dict:
    queryset = Menu.objects.filter(name=filter).prefetch_related('link')[0].link.all().order_by('position')
    menu = {}

    for item in queryset:
        if not item.parent:
            menu[item.name] = {
                'slug': item.url,
                'children': []
            }
        else:
            menu[item.parent.name]['children'].append(item)

    return {'queryset': menu, 'filter': filter}