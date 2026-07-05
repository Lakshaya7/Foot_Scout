from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, MatchViewSet, ScoutReportViewSet

# The DefaultRouter automatically generates the standard REST URLs 
# (GET /players/, POST /players/, GET /players/1/, etc.)
router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'reports', ScoutReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
]