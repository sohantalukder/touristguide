# Generated by Django 3.2.10 on 2021-12-21 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourist', '0004_remove_guider_ratting'),
    ]

    operations = [
        migrations.CreateModel(
            name='hireguider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(default='', max_length=500)),
                ('ammount', models.FloatField(default=0.0, max_length=100)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tourist.guider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
