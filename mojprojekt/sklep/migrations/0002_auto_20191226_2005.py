# Generated by Django 2.2.7 on 2019-12-26 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('delivery', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklep.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_products',
            field=models.ManyToManyField(through='sklep.OrderedProduct', to='sklep.Product'),
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name=range(1, 5))),
                ('message', models.CharField(max_length=400)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklep.Product')),
            ],
        ),
    ]
