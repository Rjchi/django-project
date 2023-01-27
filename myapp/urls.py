# Este archivo se creo con el fin de que cada aplicacion contenga sus propias rutas

from django.urls import path
# Asi importamos todo el archivo:
# Y para hacer uso ya sea de sus funciones se pone views.LoQueQuiero
from myapp import views
# El punto es para referirce a la ruta actual (en este caso es myapp)
from . import views

#  Aqui tenemos las urls que vamos a utilizar
urlpatterns = [
    path('', views.index),
    # Con esto decimos que entre en la ruta 'ruta/ruta.com/' y que ejecute una funcion que esta dentro de views
    # esta funcion actua como un documento html en este caso (por asi decirlo)
    path('about/', views.about),
    # Con esto lo que hacemos es crear una variable que esperamos, y extraerla con la funcion
    # tambien podemos hacerlo con un int ejm: hello/<int:id>
    path('hello/<str:usuario>', views.unaFuncion),

    path('projects/', views.projectos),
    path('task/', views.tareas)
]