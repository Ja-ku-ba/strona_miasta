# Generated by Django 4.1.4 on 2023-01-17 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_usernotifications_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usernotifications',
            options={},
        ),
        migrations.RemoveField(
            model_name='usernotifications',
            name='added',
        ),
    ]