# Generated by Django 3.2.5 on 2021-08-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_data_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cost',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
