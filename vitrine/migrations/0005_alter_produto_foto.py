# Generated by Django 4.2.2 on 2023-06-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0004_rename_criacaoem_produto_criadoem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/<django.db.models.fields.IntegerField>'),
        ),
    ]
