# Generated by Django 4.2 on 2023-06-28 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='AmountPaid',
            new_name='amountpaid',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='DateofDelivery',
            new_name='dateofdelivery',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='DateofShipping',
            new_name='dateofshipping',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='PendingAmount',
            new_name='pendingamount',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='ShippingMode',
            new_name='shippingmode',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='Status',
            new_name='status',
        ),
    ]
