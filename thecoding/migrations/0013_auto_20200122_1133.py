# Generated by Django 2.2.6 on 2020-01-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0012_auto_20200122_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='addressId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='block',
            name='blockId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='developer',
            name='DevId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
