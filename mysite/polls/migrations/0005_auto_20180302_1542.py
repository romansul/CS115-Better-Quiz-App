# Generated by Django 2.0.1 on 2018-03-02 23:42

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('admin', '0005_auto_20180302_1520'),
        ('polls', '0004_auto_20180302_1520'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
    ]
