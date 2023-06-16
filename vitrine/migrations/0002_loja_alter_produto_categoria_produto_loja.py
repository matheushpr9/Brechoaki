# Generated by Django 4.2.2 on 2023-06-15 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('nomeFantasia', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino'), ('INFANTIL', 'Infantil'), ('UNISEX', 'Unisex')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='produto',
            name='loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vitrine.loja'),
            preserve_default=False,
        ),
    ]
