# Generated by Django 4.0.1 on 2022-02-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0014_alter_request_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(default='Not start yet', max_length=100),
        ),
    ]
