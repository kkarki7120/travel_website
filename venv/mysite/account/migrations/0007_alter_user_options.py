# Generated by Django 4.0.4 on 2022-04-15 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
