from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamTestCase(TestCase):
    def setUp(self):
        user = User(username="teamuser", email="teamuser@example.com", password="password123").save()
        team = Team(name="Test Team", members=[user]).save()

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(len(team.members), 1)

class ActivityTestCase(TestCase):
    def setUp(self):
        user = User(username="activityuser", email="activityuser@example.com", password="password123").save()
        Activity(user=user, activity_type="Running", duration="01:00:00").save()

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, "01:00:00")

class LeaderboardTestCase(TestCase):
    def setUp(self):
        user = User(username="leaderboarduser", email="leaderboarduser@example.com", password="password123").save()
        Leaderboard(user=user, score=100).save()

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.user.username, "leaderboarduser")

class WorkoutTestCase(TestCase):
    def setUp(self):
        Workout(name="Yoga", description="Morning Yoga Session").save()

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Yoga")
        self.assertEqual(workout.description, "Morning Yoga Session")
