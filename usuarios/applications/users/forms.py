from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
        )
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','No coinciden las contraseñas...')
            
class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usernme',
                'style': '{ margin: 10px }',
            }
        )
    )
    
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
        
    password1 = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa Contraseña Actual...'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingresa Nueva Contraseña...'
            }
        )
    )
    
class VerificationForm(forms.Form):
    codregistro = forms.CharField(
        label='Codigo',
        required=True,
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa codigo...'
            }
        )
    )
    
    def __init__(self,pk, *args, **kwargs):
            self.id_user = pk
            super(VerificationForm, self).__init__(*args, **kwargs)
    
    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']
        
        if len(codigo) == 6:
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('Codigo invalido...')
        
        else:
            raise forms.ValidationError('Codigo invalido...')
        