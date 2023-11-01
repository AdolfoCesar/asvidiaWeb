from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('quienes-somos.html', views.quienesSomos, name='quienes-somos'),
    path('estatutos.html', views.estatutos, name='estatutos'),
    path('miembros.html', views.miembros, name='miembros'),

    path('conferencias.html', views.conferencias, name='conferencias'),
    path('cursillos.html', views.cursillos, name='cursillos'),
    path('excursiones.html', views.excursiones, name='excursiones'),
    path('colonias.html', views.colonias, name='colonias'),
    path('convivencias.html', views.convivencias, name='convivencias'),
    path('talleres.html', views.talleres, name='talleres'),
    path('acompaniamientos.html', views.acompaniamientos, name='acompaniamientos'),
    path('pautas.html', views.pautas, name='pautas'),
    path('circular.html', views.circular, name='circular'),
    path('carol.html', views.carol, name='carol'),
    path('diabetes-t1.html', views.diabetesT1, name='diabetes-t1'),
    path('diabetes-t2.html', views.diabetesT2, name='diabetes-t2'),
]
