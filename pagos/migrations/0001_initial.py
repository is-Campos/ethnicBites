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
            name='MetodoDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('fecha', models.DateTimeField(verbose_name='fecha pago')),
                ('idCliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('idMetodoDePago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagos.metododepago')),
            ],
        ),
    ]
