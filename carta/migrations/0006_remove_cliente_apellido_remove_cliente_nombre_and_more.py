# Generated by Django 4.0.3 on 2024-06-21 23:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carta', '0005_alter_item_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pedido',
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carta.cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]