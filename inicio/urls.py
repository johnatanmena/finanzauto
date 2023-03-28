from django.urls import include, path
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('watson', (lista.as_view()), name='chatbots_list'),
    path('cargue', (cargue.as_view()), name='carga_view')
]
