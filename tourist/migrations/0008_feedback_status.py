# Generated by Django 3.2.10 on 2021-12-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0007_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]