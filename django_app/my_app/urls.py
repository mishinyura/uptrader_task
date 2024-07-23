from django.urls import path
from .views import showIndex

urlpatterns = [
    path('', showIndex, name='index'),
]
