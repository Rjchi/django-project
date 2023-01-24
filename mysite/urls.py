from django.contrib import admin
from django.urls import path
# Asi importamos todo el archivo:
# Y para hacer uso ya sea de sus funciones se pone views.LoQueQuiero
# from myapp import views
from myapp.views import unaFuncion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', unaFuncion)
]
