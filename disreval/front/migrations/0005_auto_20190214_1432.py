# Generated by Django 2.1.3 on 2019-02-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20190214_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='numero',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='cargo',
            new_name='role',
        ),
    ]