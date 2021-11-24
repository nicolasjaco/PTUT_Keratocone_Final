from django.urls import path

from . import views
from .controller.kera_controller import handle
from .controller import suivi_controller

urlpatterns = [
    path('', views.index, name='index'),
    path('kera/<str:methode>',handle,name='POST_kera'),
    path('suivi/<str:age>/<str:consultation>/<str:KC>',suivi_controller.handle,name='POST_suivi'),
]