# Generated by Django 4.2 on 2024-03-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen_med',
            name='cod_orden',
            field=models.IntegerField(blank=True, null=True, verbose_name='Orden'),
        ),
    ]