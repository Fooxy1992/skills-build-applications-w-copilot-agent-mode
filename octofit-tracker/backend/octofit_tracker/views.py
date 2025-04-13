from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/'
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
