# Generated by Django 2.2.7 on 2019-11-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0002_auto_20191128_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('delivery', models.CharField(max_length=100)),
            ],
        ),
    ]
