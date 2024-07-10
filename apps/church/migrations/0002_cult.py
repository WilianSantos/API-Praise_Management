# Generated by Django 4.2 on 2024-07-10 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(default=datetime.datetime)),
                ('preacher', models.CharField(blank=True, max_length=50, null=True)),
                ('church', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='church_cult', to='church.church')),
            ],
        ),
    ]