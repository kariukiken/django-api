# Generated by Django 3.2.17 on 2023-02-25 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230220_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='issue_to',
        ),
    ]
