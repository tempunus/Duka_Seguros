from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario

class UserRegisterForm(UserCreationForm):
    """Formulário personalizado para registro de usuários"""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False, label='Nome')
    last_name = forms.CharField(max_length=30, required=False, label='Sobrenome')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar senha'


class UserUpdateForm(forms.ModelForm):
    """Formulário para atualização de dados do usuário"""
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False, label='Nome')
    last_name = forms.CharField(max_length=30, required=False, label='Sobrenome')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'


class ProfileUpdateForm(forms.ModelForm):
    """Formulário para atualização do perfil do usuário"""
    class Meta:
        model = PerfilUsuario
        fields = ['cargo', 'telefone', 'foto']
        labels = {
            'cargo': 'Cargo',
            'telefone': 'Telefone',
            'foto': 'Foto de perfil'
        }
