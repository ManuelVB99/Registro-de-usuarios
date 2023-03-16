from django import forms

class EditarClientes(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()
    fecha_registro = forms.DateField()