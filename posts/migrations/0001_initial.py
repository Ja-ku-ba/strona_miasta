# Generated by Django 4.1.4 on 2023-01-04 13:25

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=256)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Interractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=posts.models.get_image_filepath)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('reactions', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
