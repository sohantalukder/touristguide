# Generated by Django 3.2.10 on 2021-12-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0045_auto_20211228_0348'),
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
            field=models.CharField(choices=[('Accept', 'Accept'), ('Reject', 'Reject'), ('Pending', 'Pending')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100),
        ),
    ]