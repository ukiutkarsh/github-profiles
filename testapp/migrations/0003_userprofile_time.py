# Generated by Django 3.2.7 on 2021-09-17 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210917_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]