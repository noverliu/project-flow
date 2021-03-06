# Generated by Django 4.0.1 on 2022-02-11 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0007_alter_requestlog_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='assignee',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='request',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserExtensions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowableKey', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
