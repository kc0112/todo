# Generated by Django 3.2.5 on 2021-07-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='uid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
