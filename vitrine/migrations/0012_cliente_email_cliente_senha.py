# Generated by Django 4.2.2 on 2023-06-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0011_alter_produto_foto_alter_produto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]