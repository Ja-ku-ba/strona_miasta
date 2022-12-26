# Generated by Django 4.1.4 on 2022-12-26 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0003_localstaff_person_alter_localstaff_local_ovners_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.locals')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]