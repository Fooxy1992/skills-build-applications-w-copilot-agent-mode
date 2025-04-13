from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
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

class LeaderboardAPIView(APIView):
    def get(self, request):
        try:
            leaderboards = Leaderboard.objects.all()
            data = [leaderboard.to_mongo().to_dict() for leaderboard in leaderboards]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            leaderboard = Leaderboard(**request.data)
            leaderboard.save()
            return Response(leaderboard.to_mongo().to_dict(), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects
    serializer_class = WorkoutSerializer
