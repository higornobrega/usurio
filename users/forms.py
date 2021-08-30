from django.contrib.auth import forms

from .models import Colaborador 

class ColaboradorChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Colaborador

class ColaboradorCreationForm(forms.UserCreationForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Colaborador