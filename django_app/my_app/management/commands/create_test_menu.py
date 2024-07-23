from django.core.management import BaseCommand
from my_app.models import Menu, Link


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Инициализация Top Menu')
        links = {
            'Услуги': (None, '/services'),
            'Товары': (None, '/products'),
            'Блог': (None, '/blog'),
            'Контакты': (None, '/contacts'),
            'О нас': (None, '/about'),
            'Отзывы': (None, '/reviews'),
            'Выгул собак': (1, ''),
            'Выгул кошек': (1, ''),
            'Выкул коз': (1, ''),
            'Корма для собак': (2, ''),
            'Корма для кошек': (2, ''),
            'Корма для коз': (2, ''),
        }
        topmenu = Menu.objects.create(name='topmenu')
        bottommenu = Menu.objects.create(name='bottommenu')
        links_obj = []

        for key, val in links.items():
            parent = None
            if val[0]:
                parent = Link.objects.get(id=val[0])
            link = Link.objects.create(name=key, parent=parent, url=val[1])
            links_obj.append(link)

        topmenu.link.set([obj for obj in links_obj if not obj.name in ['О нас', 'Отзывы']])
        bottommenu.link.set(links_obj)
        self.stdout.write(self.style.SUCCESS(f'{topmenu.name} и {bottommenu.name} созданы'))