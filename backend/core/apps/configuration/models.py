from django.db import models

class PopularityConfig(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    popularity_per_star = models.IntegerField(blank=False, null=False)
    popularity_per_ton = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'Popularity star: {self.popularity_per_star} | Popularity ton: {self.popularity_per_ton}'