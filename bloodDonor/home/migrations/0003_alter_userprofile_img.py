# Generated by Django 4.2.4 on 2023-08-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_userprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]
