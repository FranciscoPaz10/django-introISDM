# Generated by Django 3.2.2 on 2024-09-23 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proyectofinalpp', '0002_auto_20240826_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_Empleados', models.AutoField(primary_key=True, serialize=False)),
                ('Telefono', models.IntegerField()),
                ('No_Documento', models.IntegerField()),
                ('Direccion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProdProv',
            fields=[
                ('id_prod_prov', models.AutoField(primary_key=True, serialize=False)),
                ('idProducto', models.IntegerField()),
                ('id_proveedor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('CUIT', models.IntegerField()),
                ('Telefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=45)),
                ('Domicilio', models.CharField(max_length=45)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='TipoPersona',
        ),
        migrations.RenameField(
            model_name='caja',
            old_name='Saldo',
            new_name='Saldo_inicial',
        ),
        migrations.RenameField(
            model_name='caja',
            old_name='id_Tipo',
            new_name='id_Empleados',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='idCajas',
            new_name='Nro_Compra',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='idCompra',
            new_name='idCompras',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='id_Persona',
            new_name='id_proveedor',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='Fecha_venta',
            new_name='VENT_AtGral',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='Fecha_Compra',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='Total_Compra',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='idMarca',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='Met_pagos',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='idCajas',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_Persona',
        ),
        migrations.AddField(
            model_name='compra',
            name='Cantidad',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Fecha_hora_compra',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Metodo_pago',
            field=models.CharField(default='efectivo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Precio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Producto',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Total_compra',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='Marca',
            field=models.CharField(default='Sin marca', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Fecha_hora_venta',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Garantias',
            field=models.CharField(default='Sin garantía', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Metodo_pago',
            field=models.CharField(default='efectivo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Precio_uni',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Productos',
            field=models.CharField(default='Sin producto', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Usuario',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='Prec_uni',
            field=models.FloatField(),
        ),
    ]
