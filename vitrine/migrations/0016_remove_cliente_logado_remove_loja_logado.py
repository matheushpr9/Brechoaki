# Generated by Django 4.2.2 on 2023-06-26 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0015_cliente_logado_loja_logado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='logado',
        ),
        migrations.RemoveField(
            model_name='loja',
            name='logado',
        ),
    ]
