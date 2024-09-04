# Generated by Django 4.0.3 on 2024-09-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0017_delete_estadopedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('confirmado', 'confirmado'), ('en_preparacion', 'En preparación'), ('listo_para_entregar', 'Listo para entregar'), ('entregado', 'entregado'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], default='confirmado', max_length=25),
        ),
    ]