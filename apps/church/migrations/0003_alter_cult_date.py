# Generated by Django 4.2 on 2024-07-20 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_cult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cult',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
