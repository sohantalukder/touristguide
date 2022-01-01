# Generated by Django 3.2.10 on 2021-12-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0010_feedback_love'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
