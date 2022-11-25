from django import forms 
from django.db import models

class UsuarioForm(forms.ModelForm): 
    
    fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']