# Generated by Django 5.1 on 2024-08-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configurator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=15)),
                ('area', models.IntegerField()),
                ('number_of_outlets', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
