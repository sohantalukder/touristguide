# Generated by Django 3.2.10 on 2021-12-22 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0042_alter_admintouristevent_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Reject', 'Reject'), ('Pending', 'Pending'), ('Accept', 'Accept')], default='Pending', max_length=100),
        ),
    ]
