from django.db import models
from django.contrib.auth.models import AbstractUser


class Colaborador(AbstractUser):
    first_name = models.CharField('Primerio Nome', max_length=250, default='')
    last_name = models.CharField('Sobrenome', max_length=250, default='')
    tipo = models.CharField('Tipo', max_length=250)
    email = models.EmailField('Email Institucional', max_length=250, default='unifop@fiponline.edu.br')
    numeroTelefone = models.CharField('Número Telefone', max_length=20)
    setor = models.CharField('Nome do Setor', max_length=250, null=True, blank=True)
    instagram = models.CharField('Instagram', max_length=250, blank=True, null=True)
    linkedin = models.CharField('Linkedin', max_length=250, blank=True, null=True)
    lates = models.CharField('Curriculo Lates', max_length=250, blank=True, null=True)
    image = models.CharField('Imagem', max_length=250, blank=True, null=True)