# Generated by Django 4.0.1 on 2022-02-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_request_assignee_request_published_userextensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='processInstanceId',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='requestlog',
            name='operator',
            field=models.CharField(default='sys', max_length=200),
        ),
    ]