# Generated by Django 3.1.3 on 2020-12-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premium',
            name='subscription_type',
        ),
        migrations.AddField(
            model_name='user_subscription',
            name='date_of_last_payment',
            field=models.DateField(null=True),
        ),
    ]
