# Generated by Django 3.2.6 on 2021-08-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_colaborador_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='nomeColaborador',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='lastName',
            field=models.CharField(default='', max_length=250, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='first_name',
            field=models.CharField(default='', max_length=250, verbose_name='Primerio Nome'),
        ),
    ]