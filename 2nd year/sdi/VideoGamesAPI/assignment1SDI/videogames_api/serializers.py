from rest_framework import serializers

from .models import *


class VideoGameSerializer(serializers.ModelSerializer):
    game_avg_year = serializers.IntegerField(read_only=True)

    class Meta:
        model = VideoGame
        fields = '__all__'

    # def validate_rating(self, value):
    #     if value > 5 or value < 1:
    #         raise serializers.ValidationError("Rating must be between 1 and 5!")
    #     return value


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

    # def validate_activeUsers(self, value):
    #     if value < 2:
    #         raise serializers.ValidationError("There cannot be less than one active user!")
    #     return value


class PlayerSerializer(serializers.ModelSerializer):
    player_avg_age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'

    # def validate_age(self, value):
    #     if value < 13:
    #         raise serializers.ValidationError("We are not allowed to collect your data if you're that young.")
    #     return value


class PlayerGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGame
        fields = '__all__'
