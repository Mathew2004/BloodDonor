# Generated by Django 4.2.4 on 2023-08-19 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_userprofile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]