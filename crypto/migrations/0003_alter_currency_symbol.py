# Generated by Django 3.2.25 on 2024-05-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20240523_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
