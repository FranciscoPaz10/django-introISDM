# Generated by Django 3.2.2 on 2024-10-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinalpp', '0012_alter_empleado_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='Saldo_final',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
