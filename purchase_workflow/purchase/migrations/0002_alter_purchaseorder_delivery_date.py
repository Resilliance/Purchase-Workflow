# Generated by Django 4.2.2 on 2023-06-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateField(blank=True, verbose_name='Delivery Date'),
        ),
    ]
