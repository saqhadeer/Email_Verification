# Generated by Django 2.0.4 on 2018-04-25 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_profile_email_confirmation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_confirmation',
            new_name='email_confirmed',
        ),
    ]
