# Generated by Django 3.2.10 on 2021-12-20 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0003_alter_guider_ratting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guider',
            name='ratting',
        ),
    ]
