import uuid

from django.contrib.auth.models import User
from django.db import models


class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500, null=True)
    activeUsers = models.PositiveIntegerField(null=True)
    screen = models.BooleanField(default=True)
    handheld = models.BooleanField(default=True)
    size = models.PositiveSmallIntegerField(null=True)

    class Meta:
        db_table = "platform"
        ordering = ['-name']

    def __str__(self):
        return f"Platform: {self.name}"


class VideoGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    releaseYear = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, null=True)
    company = models.CharField(max_length=50)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, to_field='id')
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "videogame"
        ordering = ['-name']

    def __str__(self):
        return f"Game: {self.name}"


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=10, null=True)
    age = models.PositiveSmallIntegerField(default=18)
    description = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=2, default="NB")
    favouriteGenre = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "player"
        ordering = ['-username']

    def __str__(self):
        return f"Player: {self.username}"


class PlayerGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(Player, on_delete=models.CASCADE)
    gamename = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True)
    hoursPlayed = models.SmallIntegerField(default=0)
    hasSaveFile = models.BooleanField(default=False)

    class Meta:
        db_table = "playergame"
        ordering = ['-username']

    def __str__(self):
        return f"Game owned by Player data: {self.username} + {self.gamename}"
