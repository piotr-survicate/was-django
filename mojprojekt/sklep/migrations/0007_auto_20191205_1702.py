# Generated by Django 2.2.7 on 2019-12-05 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0006_auto_20191205_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklep.Order'),
        ),
    ]
