# Generated by Django 4.0.1 on 2022-03-17 21:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_remove_ledger_organisation_ledger_address_one_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communications', '0002_alter_cummunication_kind'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cummunication',
            new_name='Communication',
        ),
    ]
