# Generated by Django 2.1 on 2018-11-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20181115_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worklocation',
            name='id',
        ),
        migrations.AlterField(
            model_name='worklocation',
            name='work_location',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
