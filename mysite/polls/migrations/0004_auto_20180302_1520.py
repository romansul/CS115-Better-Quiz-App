# Generated by Django 2.0.1 on 2018-03-02 23:20

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('admin', '0005_auto_20180302_1520'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('polls', '0003_studentuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentUser',
            new_name='User',
        ),
    ]
