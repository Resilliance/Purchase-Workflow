# Generated by Django 4.2.2 on 2023-06-21 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_alter_vendor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='vendor',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='street_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address 1'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='street_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address 2'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.country'),
        ),
    ]