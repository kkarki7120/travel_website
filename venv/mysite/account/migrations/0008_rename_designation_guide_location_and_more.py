# Generated by Django 4.0.4 on 2022-04-16 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='designation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_employee',
            new_name='is_guide',
        ),
    ]
