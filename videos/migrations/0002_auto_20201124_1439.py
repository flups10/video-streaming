# Generated by Django 3.1.3 on 2020-11-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Episodes',
            new_name='Episode',
        ),
        migrations.RenameModel(
            old_name='Series',
            new_name='Serie',
        ),
    ]
