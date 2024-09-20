from django import forms
from .models import Edicao, Noticia, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['data', 'titulo']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de Publicação'}),
        }
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['edicao', 'titulo', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None