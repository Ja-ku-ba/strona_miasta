# Generated by Django 4.1.4 on 2023-01-04 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagesroom',
            options={'ordering': ['-created']},
        ),
    ]
