# Generated by Django 5.1.1 on 2024-12-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_gamehistory_date_played_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamehistory',
            name='game_settings',
            field=models.CharField(default=60, max_length=100),
            preserve_default=False,
        ),
    ]