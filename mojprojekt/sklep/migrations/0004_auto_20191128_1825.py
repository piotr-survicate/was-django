# Generated by Django 2.2.7 on 2019-11-28 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastName',
        ),
    ]
