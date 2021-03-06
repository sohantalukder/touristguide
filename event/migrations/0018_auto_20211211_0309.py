# Generated by Django 3.2.10 on 2021-12-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_auto_20211211_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100),
        ),
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Reject', 'Reject'), ('Pending', 'Pending'), ('Accept', 'Accept')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100),
        ),
    ]
