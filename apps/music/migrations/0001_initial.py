# Generated by Django 4.2 on 2024-07-10 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_music', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('music_text', models.TextField()),
                ('theme', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicChord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chord', models.CharField(max_length=10)),
                ('chord_image', models.ImageField(blank=True, upload_to='chord_image/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='VersionMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('music_link', models.URLField(blank=True, max_length=255)),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Music', to='music.music')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='music_chord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MusicChord', to='music.musicchord'),
        ),
    ]