# Generated by Django 4.0.4 on 2022-04-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_guide_work_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name']},
        ),
    ]
