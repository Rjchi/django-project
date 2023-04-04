# Para crear formularios por medio de django

from django import forms

# Este codigo solo crea los inputs por mi si queremos un boton lo debemos crear en el documento html
class create_new_task(forms.Form):
    # con esto el DOM lo va a transformar en un input de tipo texto
    title = forms.CharField(label="Titulo de tares", max_length=200, required=True)
    # Lo que es title y description en el dom se van a convertir en valores para el atributo name=''
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'textArea'}), label="Descripcion de la tarea", required=True)


class create_new_project(forms.Form):
    # Para poder agregarle estilos se utiliza una propiedad llamada widget=
    # attrs={} (significa un atributo con la clase ...)
    name = forms.CharField(label='Nombre del proyecto', max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class' : 'input'}))