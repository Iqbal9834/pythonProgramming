# Generated by Django 2.2.6 on 2020-01-21 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0005_address_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='developer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thecoding.Developer'),
        ),
    ]
