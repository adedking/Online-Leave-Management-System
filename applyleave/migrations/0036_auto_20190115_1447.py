# Generated by Django 2.1.5 on 2019-01-15 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0035_auto_20181231_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='reporting_manager_empid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 47, 53, 30331), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 47, 53, 31331), null=True),
        ),
    ]
