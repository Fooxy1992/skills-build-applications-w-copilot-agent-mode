from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://potential-halibut-9gw4ggqvxv5h99v-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })

class UserViewSet(ModelViewSet):
    queryset = User.objects  # Use mongoengine's objects manager
    serializer_class = UserSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects  # Use mongoengine's objects manager
    serializer_class = TeamSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects
    serializer_class = ActivitySerializer

class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects
    serializer_class = WorkoutSerializer
