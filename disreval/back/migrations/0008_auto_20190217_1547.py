# Generated by Django 2.1.5 on 2019-02-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_auto_20190217_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=2),
        ),
    ]
