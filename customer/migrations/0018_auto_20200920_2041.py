# Generated by Django 3.1 on 2020-09-20 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20200920_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 9, 20, 20, 41, 54, 746780)),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 20, 20, 41, 54, 746780)),
        ),
    ]