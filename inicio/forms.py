from django import froms 

class FormularioCreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.integerField()