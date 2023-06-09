# Generated by Django 4.0.4 on 2022-04-24 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_remove_customer_password_remove_customer_username'),
        ('product', '0002_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='thumbnail',
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('discount', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('book_status', models.CharField(choices=[('Booking Received', 'Booking Received'), ('Booking Processing', 'Booking Processing'), ('Booking Completed', 'Booking Completed'), ('Booking Canceled', 'Booking Canceled')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
            ],
        ),
    ]
