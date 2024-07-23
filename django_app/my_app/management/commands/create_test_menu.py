from django.core.management import BaseCommand
from my_app.models import Menu, Link


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Инициализация Top Menu')
        links = {
            'Главная': (None, '/'),
            'Услуги': (None, '/services'),
            'Выгул собак': (2, ''),
            'Выгул кошек': (2, ''),
            'Выкул коз': (2, ''),
            'Товары': (None, '/products'),
            'Корма для собак': (6, ''),
            'Корма для кошек': (6, ''),
            'Корма для коз': (6, ''),
            'Блог': (None, '/blog'),
            'О нас': (None, '/about'),
            'Контакты': (None, '/contacts'),
            'Отзывы': (None, '/reviews'),
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