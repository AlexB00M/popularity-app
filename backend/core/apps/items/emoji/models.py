from django.db import models

class Emoji(models.Model):
    # Gift data
    id = models.IntegerField(primary_key=True)
    offset = models.IntegerField()
    length = models.PositiveIntegerField() 
    animated = models.BooleanField()

    image = models.ImageField(upload_to='emojis/', blank=True, null=True)
    animation_json = models.JSONField(blank=True, null=True)  

    def __str__(self):
        return str(self.id)