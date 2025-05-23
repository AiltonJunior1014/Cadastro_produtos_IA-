# Generated by Django 4.2.15 on 2024-08-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_info',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='product',
            name='product_measure',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_descrition',
            field=models.CharField(default='', max_length=200),
        ),
    ]
