# Generated by Django 5.0.6 on 2024-07-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_singer_created_at_alter_song_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
