# Generated by Django 4.2 on 2024-07-10 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='music_chord',
        ),
        migrations.AlterField(
            model_name='versionmusic',
            name='music',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='version_music', to='music.music'),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ManyToManyField(to='music.music')),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='music_chord',
            field=models.ManyToManyField(to='music.musicchord'),
        ),
    ]
