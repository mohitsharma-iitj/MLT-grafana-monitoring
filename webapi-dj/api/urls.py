from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('multiply', views.multiply, name='multiply'),
    path('echo', views.echo, name='echo'),
    path('health', views.health_check, name='health'),
]