# Generated by Django 3.2.5 on 2021-08-02 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_data_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='price',
        ),
    ]
