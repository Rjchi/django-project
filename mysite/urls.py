from django.contrib import admin
# Include es para incluir un bloque de urls que vienen de una aplicacion
from django.urls import path, include

urlpatterns = [
    # mysite Es el nucleo del proyecto
    path('admin/', admin.site.urls),
    # Include recibe como parametro el nombre de las urls que queremos importar
    path('', include('myapp.urls'))
]
