# Generated by Django 4.0.1 on 2022-01-30 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='organisation',
        ),
    ]
