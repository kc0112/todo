# Generated by Django 3.2.5 on 2021-07-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskmanager', '0002_task_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
