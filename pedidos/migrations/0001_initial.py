# Generated by Django 4.2.5 on 2023-11-12 06:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0004_alter_direccion_codigopostal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='fecha pedido')),
                ('idCliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('idDireccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('idProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.producto')),
            ],
        ),
    ]
