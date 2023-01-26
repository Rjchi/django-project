# Este archivo se creo con el fin de que cada aplicacion contenga sus propias rutas

from django.urls import path
# Asi importamos todo el archivo:
# Y para hacer uso ya sea de sus funciones se pone views.LoQueQuiero
from myapp import views
# El punto es para referirce a la ruta actual (en este caso es myapp)
from . import views

urlpatterns = [
    path('', views.unaFuncion),
    # Con esto decimos que entre en la ruta 'ruta/ruta.com/ y que ejecute una funcion que esta dentro de views
    # esta funcion actua como un documento html en este caso (por asi decirlo) 
    path('about/', views.about)
]