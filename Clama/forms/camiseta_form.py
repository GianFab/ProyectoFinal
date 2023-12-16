from django import forms


class CamisetaForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.DecimalField()
    descripcion = forms.CharField(widget=forms.Textarea())
    oferta = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False)
    codigo_camiseta = forms.CharField()
    talla = forms.CharField()
    color = forms.CharField()

class BusquedaCamisetaForm(forms.Form):
    codigo_camiseta = forms.CharField()

