# Generated by Django 4.2 on 2024-07-21 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_alter_cult_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('church', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fuction_church', to='church.church')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('availability', models.BooleanField(default=True)),
                ('cell_phone', models.CharField(max_length=14)),
                ('is_member', models.BooleanField(default=False)),
                ('church', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_church', to='church.church')),
                ('function', models.ManyToManyField(to='church.function')),
            ],
        ),
    ]
