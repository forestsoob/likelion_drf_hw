# Generated by Django 5.0.6 on 2024-07-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_singer_created_at_singer_updated_at_song_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]