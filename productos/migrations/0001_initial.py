# Generated by Django 4.2.5 on 2023-11-12 06:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('precio', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('tipo', models.CharField(max_length=100)),
                ('idVendedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
