# Generated by Django 4.1.2 on 2022-11-05 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='owner',
        ),
    ]
