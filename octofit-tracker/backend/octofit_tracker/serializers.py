from rest_framework import serializers  # Import serializers from rest_framework
from .models import User, Team, Activity, Leaderboard, Workout  # Use the User model defined in models.py
from mongoengine import Document

class MongoEngineSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def create(self, validated_data):
        return self.Meta.model(**validated_data).save()

class UserSerializer(MongoEngineSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class TeamSerializer(MongoEngineSerializer):
    class Meta:
        model = Team
        fields = ('name', 'members')

class ActivitySerializer(MongoEngineSerializer):
    class Meta:
        model = Activity
        fields = ('user', 'activity_type', 'duration')

class LeaderboardSerializer(MongoEngineSerializer):
    class Meta:
        model = Leaderboard
        fields = ('user', 'score')

class WorkoutSerializer(MongoEngineSerializer):
    class Meta:
        model = Workout
        fields = ('name', 'description')
