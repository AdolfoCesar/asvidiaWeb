from django.urls import path
from . import views

urlpatterns = [
    #path('eventos.html', views.eventos, name='eventos'),
    path('<int:year>/<str:month>', views.eventos, name='eventos')

]