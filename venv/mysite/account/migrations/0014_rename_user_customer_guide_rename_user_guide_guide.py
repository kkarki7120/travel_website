# Generated by Django 4.0.4 on 2022-04-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_customer_first_name_customer_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='guide',
        ),
        migrations.RenameField(
            model_name='guide',
            old_name='user',
            new_name='guide',
        ),
    ]
