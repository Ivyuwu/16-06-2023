# Generated by Django 4.2.2 on 2023-06-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichasapp', '0005_rename_previcion_salud_ficha_prevision_salud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='prevision_salud',
            field=models.CharField(choices=[('Fonasa', 'Fonasa'), ('Isapre', 'Isapre')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Intersexual', 'Intersexual')], max_length=200, null=True),
        ),
    ]
