from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import ColaboradorChangeForm, ColaboradorCreationForm
from .models import Colaborador


@admin.register(Colaborador)

class ColaboradorAdmin(auth_admin.UserAdmin):
    form = ColaboradorChangeForm
    add_form = ColaboradorCreationForm
    model = Colaborador
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos pesonalizados", {"fields":('tipo', 'numeroTelefone', 'setor', 'instagram', 'linkedin', 'lates', 'image', )}),
    )