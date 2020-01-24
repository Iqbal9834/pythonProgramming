# Generated by Django 2.2.6 on 2020-01-21 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0009_auto_20200121_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='developer',
        ),
        migrations.AddField(
            model_name='developer',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thecoding.Address'),
            preserve_default=False,
        ),
    ]