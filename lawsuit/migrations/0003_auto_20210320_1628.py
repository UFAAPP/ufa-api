# Generated by Django 3.1.6 on 2021-03-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawsuit', '0002_lawsuit_locker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawsuit',
            name='observation',
            field=models.TextField(null=True),
        ),
    ]
