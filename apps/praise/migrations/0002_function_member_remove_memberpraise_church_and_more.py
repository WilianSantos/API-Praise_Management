# Generated by Django 4.2 on 2024-07-21 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_alter_cult_theme'),
        ('praise', '0001_initial'),
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
                ('function', models.ManyToManyField(to='praise.function')),
            ],
        ),
        migrations.RemoveField(
            model_name='memberpraise',
            name='church',
        ),
        migrations.RemoveField(
            model_name='memberpraise',
            name='function',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='drums',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='electric_guitar',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='guitar',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='low',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='musical_keyboard',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='vocal',
        ),
        migrations.DeleteModel(
            name='FunctionPraise',
        ),
        migrations.DeleteModel(
            name='MemberPraise',
        ),
        migrations.AddField(
            model_name='cast',
            name='members',
            field=models.ManyToManyField(to='praise.member'),
        ),
    ]
