# Generated by Django 3.2.10 on 2021-12-21 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0005_hireguider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hireguider',
            old_name='place',
            new_name='guider_name',
        ),
    ]