# Generated by Django 3.1.6 on 2021-03-20 16:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lawsuit', '0003_auto_20210320_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawsuit',
            name='status',
            field=models.CharField(choices=[('PROGRESS', 'Progress'), ('ARCHIVED', 'Archived')], default='PROGRESS', max_length=10),
        ),
        migrations.AlterField(
            model_name='lawsuit',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]