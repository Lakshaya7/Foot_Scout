from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Custom User Model to handle roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('SCOUT', 'Scout'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='SCOUT')

    def __str__(self):
        return f"{self.username} ({self.role})"

# 2. Football Player Model
class Player(models.Model):
    POSITION_CHOICES = (
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    date_of_birth = models.DateField()
    current_club = models.CharField(max_length=100)
    preferred_foot = models.CharField(max_length=10, choices=(('Left', 'Left'), ('Right', 'Right'), ('Both', 'Both')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 3. Match Model
class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    competition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.competition})"

# 4. Scout Report Model (The bridge linking Scout, Player, and Match)
class ScoutReport(models.Model):
    scout = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='reports')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='reports')
    
    # Performance Attributes
    pace = models.IntegerField(default=5)
    dribbling = models.IntegerField(default=5)
    passing = models.IntegerField(default=5)
    defending = models.IntegerField(default=5)
    physicality = models.IntegerField(default=5)
    
    # Summary
    overall_rating = models.DecimalField(max_digits=3, decimal_places=1)
    scouting_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report on {self.player.name} by {self.scout.username}"