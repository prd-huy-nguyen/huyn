# Generated by Django 3.2.6 on 2021-08-07 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_customer_typecustomer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress',
            new_name='address',
        ),
    ]