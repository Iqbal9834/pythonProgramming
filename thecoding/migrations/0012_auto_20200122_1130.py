# Generated by Django 2.2.6 on 2020-01-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0011_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorplan',
            name='PlanId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
