# Generated by Django 2.1 on 2018-12-31 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0034_auto_20181214_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplicationdetails',
            name='remarks',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 31, 11, 49, 25, 857429), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 31, 11, 49, 25, 859930), null=True),
        ),
    ]
