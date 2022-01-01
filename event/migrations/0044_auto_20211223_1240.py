# Generated by Django 3.2.10 on 2021-12-23 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0043_alter_admintouristevent_publish'),
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
            field=models.CharField(choices=[('Accept', 'Accept'), ('Pending', 'Pending'), ('Reject', 'Reject')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='usertouristevent',
            name='guider_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100),
        ),
        migrations.CreateModel(
            name='EventOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(default='', max_length=500)),
                ('ammount', models.FloatField(default=0.0, max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.admintouristevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]