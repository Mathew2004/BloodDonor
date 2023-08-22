# Generated by Django 4.2.4 on 2023-08-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phn1', models.CharField(max_length=30)),
                ('phn2', models.CharField(max_length=30)),
                ('fblink', models.CharField(max_length=30)),
                ('add1', models.CharField(max_length=80)),
                ('add2', models.CharField(max_length=80)),
                ('age', models.CharField(max_length=30)),
                ('bg', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='static/img')),
            ],
        ),
    ]
