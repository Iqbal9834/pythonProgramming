# Generated by Django 2.2.6 on 2020-01-21 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thecoding', '0010_auto_20200121_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('personId', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Phoneno', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Designation', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=80)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thecoding.Address')),
                ('deve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thecoding.Developer')),
            ],
        ),
    ]
