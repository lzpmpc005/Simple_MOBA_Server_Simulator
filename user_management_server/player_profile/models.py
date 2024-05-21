from django.db import models

class Player(models.Model):
    account = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    playerLevel = models.IntegerField(null=True)
    experiencePoint = models.IntegerField(null=True)

    winCount = models.IntegerField(null=True)
    loseCount = models.IntegerField(null=True)
    matchmakingRanking = models.FloatField(null=True)
    winrate = models.FloatField(null=True)

class CharacterClass(models.Model):
    type = models.CharField(primary_key=True, max_length=255)

class Character(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    class_type = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)

    winCount = models.IntegerField(null=True)
    loseCount = models.IntegerField(null=True)
    winrate = models.FloatField(null=True)

class MatchRecord(models.Model):
    id = models.AutoField(primary_key=True)
    startTime = models.DateTimeField()
    duration = models.IntegerField()
    isValid = models.BooleanField()
    winner = models.ForeignKey(Player, related_name='winner', on_delete=models.CASCADE)
    loser = models.ForeignKey(Player, related_name='loser', on_delete=models.CASCADE)
    winner_character = models.ForeignKey(Character, related_name='winner_character', on_delete=models.CASCADE)
    loser_character = models.ForeignKey(Character, related_name='loser_character', on_delete=models.CASCADE)

    host = models.ForeignKey(Player, related_name='host', on_delete=models.CASCADE)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    sender = models.ForeignKey(Player, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, default='')

class Blacklist(models.Model):
    account = models.CharField(primary_key=True, max_length=255)
    startTime = models.DateTimeField()
    duration = models.IntegerField()
    misconduct = models.CharField(max_length=255)
