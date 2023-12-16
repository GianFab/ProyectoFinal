from django import forms


class PantalonForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.DecimalField()
    descripcion = forms.CharField(widget=forms.Textarea())
    oferta = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False)
    codigo_pantalon = forms.CharField()
    talla = forms.CharField()
    estilo = forms.CharField()

class BusquedaPantalonForm(forms.Form):
    codigo_pantalon = forms.CharField()

