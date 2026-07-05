from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Player, Match, ScoutReport

# 1. Register our Custom User
admin.site.register(User, UserAdmin)

# 2. Register Player with a custom display list
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'current_club', 'preferred_foot')
    search_fields = ('name', 'current_club')
    list_filter = ('position', 'preferred_foot')

# 3. Register Match with a custom display list
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'match_date', 'competition')
    search_fields = ('home_team', 'away_team', 'competition')
    list_filter = ('competition', 'match_date')

# 4. Register Scout Report with a custom display list
@admin.register(ScoutReport)
class ScoutReportAdmin(admin.ModelAdmin):
    list_display = ('player', 'scout', 'match', 'overall_rating', 'created_at')
    list_filter = ('overall_rating', 'created_at')
    search_fields = ('player__name', 'scout__username')