# Generated by Django 2.1.5 on 2019-02-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=models.CharField(max_length=30), upload_to='../static/'),
        ),
    ]