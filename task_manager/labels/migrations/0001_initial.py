# Generated by Django 4.0 on 2022-01-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
            ],
        ),
    ]
