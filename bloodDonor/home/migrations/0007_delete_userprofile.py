# Generated by Django 4.2.4 on 2023-08-20 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_userprofile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]