# Generated by Django 3.1.6 on 2021-02-14 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
                ('full', models.BooleanField()),
            ],
            options={
                'db_table': 'LOCKER',
            },
        ),
        migrations.CreateModel(
            name='Lawsuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('district', models.CharField(max_length=100)),
                ('court', models.CharField(choices=[('IN', 'Vara de Infância e Juventude'), ('FA', 'Vara da Fazenda Pública'), ('CI', 'Vara Civel'), ('FM', 'Vara de família'), ('CR', 'Vara Criminal'), ('ER', 'Juizado Especial Criminal'), ('AU', 'Juízes de Direito Auxiliares'), ('EC', 'Juizado Especial Cível'), ('UN', 'Vara Unica')], default='UN', max_length=2)),
                ('code_number', models.CharField(max_length=100)),
                ('descriptor', models.CharField(max_length=150)),
                ('observation', models.TextField()),
                ('identifier', models.CharField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('locker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawsuit.locker')),
            ],
            options={
                'db_table': 'LAWSUIT',
            },
        ),
    ]
