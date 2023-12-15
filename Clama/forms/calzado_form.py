from django import forms


class CalzadoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.DecimalField()
    descripcion = forms.CharField(widget=forms.Textarea())
    oferta = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False)
    codigo_calzado = forms.CharField()
    talla = forms.CharField()
    tipo = forms.CharField()

class BusquedaCalzadoForm(forms.Form):
    codigo_calzado = forms.CharField()

