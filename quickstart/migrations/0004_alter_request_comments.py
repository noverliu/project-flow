# Generated by Django 4.0.1 on 2022-02-09 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='comments',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
