from .models import Article
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','description', 'slug']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'name'}))
    password1 = forms.CharField(label='Пороль', widget=forms.TextInput(attrs={'placeholder': 'password1'}))
    password2 = forms.CharField(label='Подтверждение пороля', widget=forms.TextInput(attrs={'placeholder': 'password2'}))
    email = forms.EmailField(label='Почта',widget=forms.TextInput(attrs={'placeholder': 'email'}))

