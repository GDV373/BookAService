# Generated by Django 3.2.20 on 2023-09-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='accounts.business'),
            preserve_default=False,
        ),
    ]