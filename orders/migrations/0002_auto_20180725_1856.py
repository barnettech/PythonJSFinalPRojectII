# Generated by Django 2.0.7 on 2018-07-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]