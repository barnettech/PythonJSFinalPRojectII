# Generated by Django 2.0.7 on 2018-07-31 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20180731_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='email',
        ),
    ]