# Generated by Django 2.0.3 on 2018-03-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_notification_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user_receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
