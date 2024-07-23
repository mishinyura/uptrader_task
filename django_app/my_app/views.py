from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def showIndex(request: HttpRequest) -> HttpResponse:
    data = {
        'test': 'test'
    }
    return render(request, 'my_app/index.html', data)


# delete from my_app_menu where "id" > 0

# select * from my_app_menu_link

# TRUNCATE TABLE my_app_link RESTART IDENTITY
# my_app_menu_link_link_id_29c1126a_fk_my_app_link_id
# my_app_menu_link_menu_id_6d0bdf08_fk_my_app_menu_id