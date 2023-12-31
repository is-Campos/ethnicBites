# Generated by Django 4.2.5 on 2023-11-12 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
                ('idProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.producto')),
            ],
        ),
    ]
