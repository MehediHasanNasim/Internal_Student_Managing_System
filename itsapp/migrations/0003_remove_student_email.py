# Generated by Django 3.1.6 on 2021-06-09 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itsapp', '0002_auto_20210609_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
