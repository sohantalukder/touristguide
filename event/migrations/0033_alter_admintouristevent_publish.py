# Generated by Django 3.2.10 on 2021-12-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0032_alter_admintouristevent_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Accept', 'Accept'), ('Reject', 'Reject'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
    ]
