# Generated by Django 4.0.1 on 2022-02-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_requestlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlog',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
