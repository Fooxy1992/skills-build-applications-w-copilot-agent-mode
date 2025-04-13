import json
import os
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Use an absolute path to locate the test_data.json file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_data_path = os.path.join(base_dir, 'test_data.json')

        # Debugging output to verify the file path and contents
        self.stdout.write(f"Using test data file at: {test_data_path}")
        with open(test_data_path, 'r') as file:
            file_contents = file.read()
            self.stdout.write(f"File contents: {file_contents}")
            data = json.loads(file_contents)

        # Populate users
        for user_data in data['users']:
            User(username=user_data['username'], email=user_data['email'], password=user_data['password']).save()

        # Populate teams
        for team_data in data['teams']:
            members = [User.objects.get(username=member) for member in team_data['members']]
            Team(name=team_data['name'], members=members).save()

        # Populate activities
        for activity_data in data['activities']:
            user = User.objects.get(username=activity_data['user'])
            Activity(user=user, activity_type=activity_data['activity_type'], duration=activity_data['duration']).save()

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(username=leaderboard_data['user'])
            Leaderboard(user=user, score=leaderboard_data['score']).save()

        # Populate workouts
        for workout_data in data['workouts']:
            Workout(name=workout_data['name'], description=workout_data['description']).save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
