from django import forms


class BusquedaProductoForm(forms.Form):
    nombre = forms.CharField()

