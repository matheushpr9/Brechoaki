# Generated by Django 4.2.2 on 2023-06-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0021_alter_produto_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(max_length=5),
        ),
    ]