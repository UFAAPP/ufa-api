# Generated by Django 3.1.6 on 2021-03-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210314_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
