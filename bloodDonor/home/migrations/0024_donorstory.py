# Generated by Django 4.2.4 on 2023-08-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_userprofile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorStory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phn', models.CharField(max_length=50)),
                ('msg', models.TextField()),
                ('imgname', models.CharField(max_length=200)),
            ],
        ),
    ]
