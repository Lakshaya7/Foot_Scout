from rest_framework import serializers
from .models import User, Player, Match, ScoutReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'email']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class ScoutReportSerializer(serializers.ModelSerializer):
    # We make these read-only so the mobile app gets the nested data nicely,
    # but doesn't have to submit full string names when creating a report.
    scout_name = serializers.CharField(source='scout.username', read_only=True)
    player_name = serializers.CharField(source='player.name', read_only=True)
    match_title = serializers.CharField(source='match.__str__', read_only=True)

    class Meta:
        model = ScoutReport
        fields = '__all__'
        # The scout will be assigned automatically by the backend based on who is logged in
        read_only_fields = ['scout', 'created_at']