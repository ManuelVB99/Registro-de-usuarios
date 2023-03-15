from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class registrousuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder': 'Email'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'First Name'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label ="", widget= forms.PasswordInput(attrs={'placeholder': "Contraseña anterior"}))
    new_password1 = forms.CharField(label ="", widget= forms.PasswordInput(attrs={'placeholder': "Contraseña nueva"}))
    new_password2 = forms.CharField(label ="", widget= forms.PasswordInput(attrs={'placeholder': "Confirmar contraseña nueva"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}