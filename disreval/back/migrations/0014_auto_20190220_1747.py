# Generated by Django 2.1.5 on 2019-02-20 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0013_auto_20190217_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
