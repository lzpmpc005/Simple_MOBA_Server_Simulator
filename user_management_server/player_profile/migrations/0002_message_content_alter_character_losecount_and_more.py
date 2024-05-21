# Generated by Django 4.2.6 on 2024-05-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='character',
            name='loseCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='winCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='winrate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='loseCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='matchmakingRanking',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='winCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='winrate',
            field=models.FloatField(null=True),
        ),
    ]
