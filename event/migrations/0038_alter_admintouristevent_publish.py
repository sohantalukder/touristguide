# Generated by Django 3.2.10 on 2021-12-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0037_auto_20211220_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintouristevent',
            name='publish',
            field=models.CharField(choices=[('Reject', 'Reject'), ('Pending', 'Pending'), ('Accept', 'Accept')], default='Pending', max_length=100),
        ),
    ]