from django.forms import ModelForm, TextInput, NumberInput, Select, PasswordInput, ChoiceField
from parkapp.models import tipovehiculo, vehiculos, empleados
from django import forms

class tipovehiculoForm(ModelForm):
    class Meta:
        model = tipovehiculo
        fields = ['tarifa', 'posiciones']
        widgets = {
            'tarifa':  NumberInput(attrs={'class':'form-control'}),
            'posiciones':  NumberInput(attrs={'class':'form-control'}),
        }

class vehiculosForm(ModelForm):
    class Meta:
        model = vehiculos
        fields = ['placa', 'tipovehiculo']
        widgets = {
            'placa': TextInput(attrs={'class':'form-control'}),
            'tipovehiculo': NumberInput(attrs={'class':'form-control'}),
      }

class empleadosForm(ModelForm):
    class Meta:
        model = empleados
        fields = ['nombres', 'apellidos', 'telefono', 'usuario', 'clave']
        widgets = {
            'nombres': TextInput(attrs={'class':'form-control'}),
            'apellidos': TextInput(attrs={'class':'form-control'}),
            'telefono': TextInput(attrs={'class':'form-control'}),
            'usuario': TextInput(attrs={'class':'form-control'}),
            'clave': PasswordInput(attrs={'class':'form-control'}),
        }

class loginForm(forms.Form):
    usuario = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
    contraseña = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}))


class ticketForm(forms.Form):
    idtipos=((1, 'Moto'),(2, 'Carro'),(3, 'Bicicleta'))
    placa = forms.CharField(max_length=7,widget=TextInput(attrs={'class':'form-control'}))
    tipovehiculo = forms.IntegerField(widget=forms.Select(choices=idtipos, attrs={'class':'form-control'} ))
