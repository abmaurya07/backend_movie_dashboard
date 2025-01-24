from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    rating = models.FloatField()
    one_line = models.TextField()
    stars = models.TextField()
    votes = models.IntegerField()
    runtime = models.IntegerField()  # in minutes
    gross = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['rating']),
            models.Index(fields=['votes']),
            models.Index(fields=['gross']),
        ] 