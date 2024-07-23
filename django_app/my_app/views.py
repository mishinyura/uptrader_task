from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def showIndex(request: HttpRequest) -> HttpResponse:
    data = {
        'test': 'test'
    }
    return render(request, 'my_app/index.html', data)
