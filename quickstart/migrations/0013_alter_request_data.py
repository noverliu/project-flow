# Generated by Django 4.0.1 on 2022-02-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0012_request_project_alter_request_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]
