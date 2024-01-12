# Generated by Django 5.0.1 on 2024-01-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FailId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mail', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
