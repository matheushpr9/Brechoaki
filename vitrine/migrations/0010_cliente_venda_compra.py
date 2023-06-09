# Generated by Django 4.2.2 on 2023-06-16 21:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0009_loja_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.cliente')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.loja')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.cliente')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrine.loja')),
            ],
        ),
    ]
