# Generated by Django 3.2.10 on 2021-12-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0041_alter_admintouristevent_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Accept', 'Accept'), ('Pending', 'Pending'), ('Reject', 'Reject')], default='Pending', max_length=100),
        ),
    ]
