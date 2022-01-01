# Generated by Django 3.2.10 on 2021-12-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_topplaceorder_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='card_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='payment_status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='risk_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='transaction_date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]