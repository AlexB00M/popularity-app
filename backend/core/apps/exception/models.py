from django.db import models
from core.apps.user.models import User
from django.utils import timezone

class LoggedException(models.Model):
    # Gift data
    id = models.AutoField(primary_key=True)  
    timestamp = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{str(self.id)} {self.user if self.user else ''} - {self.text}"