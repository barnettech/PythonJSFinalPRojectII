# Generated by Django 2.0.7 on 2018-07-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180726_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='choose_toppings',
            field=models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('NO', 'no')], default='NO', max_length=50),
        ),
    ]