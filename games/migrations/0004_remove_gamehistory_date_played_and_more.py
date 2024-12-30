# Generated by Django 5.1.1 on 2024-12-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gamehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamehistory',
            name='date_played',
        ),
        migrations.AddField(
            model_name='gamehistory',
            name='time_taken',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]