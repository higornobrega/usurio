# Generated by Django 3.2.6 on 2021-08-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210830_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='last_name',
            field=models.CharField(default='', max_length=250, verbose_name='Sobrenome'),
        ),
    ]