# Generated by Django 4.0.4 on 2022-04-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_cartproduct_product_productimage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='ordering',
        ),
    ]
