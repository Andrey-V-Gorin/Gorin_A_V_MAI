# Generated by Django 5.1.4 on 2025-01-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
