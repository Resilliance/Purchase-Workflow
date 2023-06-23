# Generated by Django 4.2.2 on 2023-06-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_alter_product_description_alter_product_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.IntegerField(null=True, verbose_name='Available Quantity'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_type',
            field=models.CharField(choices=[('stor', 'Storable'), ('cons', 'Consumable'), ('serv', 'Service')], default='stor', max_length=4),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='product',
            name='reserved_quantity',
            field=models.IntegerField(null=True, verbose_name='Reserved Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier_ids',
            field=models.ManyToManyField(to='purchase.vendor'),
        ),
    ]