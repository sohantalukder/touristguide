# Generated by Django 3.2.10 on 2021-12-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0038_alter_admintouristevent_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='Yes', max_length=100),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='Yes', max_length=100),
        ),
    ]
