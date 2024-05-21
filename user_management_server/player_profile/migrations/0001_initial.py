# Generated by Django 4.2.6 on 2024-05-18 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('account', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('misconduct', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('class_type', models.CharField(max_length=255)),
                ('winCount', models.IntegerField()),
                ('loseCount', models.IntegerField()),
                ('winrate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('account', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('playerLevel', models.IntegerField()),
                ('experiencePoint', models.IntegerField()),
                ('winCount', models.IntegerField()),
                ('loseCount', models.IntegerField()),
                ('matchmakingRanking', models.FloatField()),
                ('winrate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_profile.player')),
            ],
        ),
        migrations.CreateModel(
            name='MatchRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('isValid', models.BooleanField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='player_profile.player')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='player_profile.player')),
                ('loser_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser_character', to='player_profile.character')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='player_profile.player')),
                ('winner_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner_character', to='player_profile.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_profile.player'),
        ),
    ]