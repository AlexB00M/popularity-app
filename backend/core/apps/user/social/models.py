from django.db import models
from core.apps.user.models import User

class SocialLink(models.Model):
    SOCIAL_CHOICES = [
        ('telegram', 'Telegram'),
        ('youtube', 'Youtube'),
        ('instagram', 'Instagram')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50, choices=SOCIAL_CHOICES)
    url = models.URLField()
    
    class Meta:
        unique_together = ('user', 'platform')

    def __str__(self):
        return f'{self.user.user_name} - {self.platform}'