# Generated by Django 3.2.17 on 2023-02-20 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='phone_number',
        ),
    ]
