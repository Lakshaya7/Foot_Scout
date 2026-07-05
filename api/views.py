from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Player, Match, ScoutReport
from .serializers import PlayerSerializer, MatchSerializer, ScoutReportSerializer
from .permissions import IsAdminOrReadOnly

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class ScoutReportViewSet(viewsets.ModelViewSet):
    serializer_class = ScoutReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Security check: 
        Admins can see ALL reports.
        Scouts can ONLY see the reports they created themselves.
        """
        user = self.request.user
        if user.role == 'ADMIN':
            return ScoutReport.objects.all()
        return ScoutReport.objects.filter(scout=user)

    def perform_create(self, serializer):
        """
        When a mobile app sends a POST request to create a report,
        we automatically assign the logged-in user as the scout.
        """
        serializer.save(scout=self.request.user)