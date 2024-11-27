# Generated by Django 5.1.3 on 2024-11-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=14)),
                ('Instrument_type', models.CharField(max_length=30)),
            ],
        ),
    ]