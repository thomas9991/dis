# Generated by Django 2.1.5 on 2019-02-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_contact', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('phone', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('desc_role', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.Role'),
        ),
    ]
