# Generated by Django 3.2.10 on 2021-12-22 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourist', '0009_alter_feedback_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='love',
            field=models.ManyToManyField(blank=True, related_name='scope_love', to=settings.AUTH_USER_MODEL),
        ),
    ]
