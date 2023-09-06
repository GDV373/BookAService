# Generated by Django 3.2.20 on 2023-09-05 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230829_0840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bcust',
            new_name='BusinessCustomer',
        ),
        migrations.RenameModel(
            old_name='CarDB',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='Cust',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='businesscustomer',
            old_name='cars',
            new_name='carFK',
        ),
        migrations.RenameField(
            model_name='businesscustomer',
            old_name='customer',
            new_name='customerFK',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cars',
            new_name='carFK',
        ),
        migrations.AlterModelTable(
            name='businesscustomer',
            table=None,
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]