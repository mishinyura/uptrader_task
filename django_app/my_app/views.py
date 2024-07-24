from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def showIndex(request: HttpRequest) -> HttpResponse:
    return render(request, 'my_app/index.html')