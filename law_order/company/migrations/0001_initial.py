# Generated by Django 3.1.6 on 2021-02-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_number', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
