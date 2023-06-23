# Generated by Django 4.2.2 on 2023-06-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.FloatField(null=True, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(null=True, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier_ids',
            field=models.ManyToManyField(null=True, to='purchase.vendor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.FloatField(null=True, verbose_name='Volume'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(null=True, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(null=True, verbose_name='Width'),
        ),
    ]
