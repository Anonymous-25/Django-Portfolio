from django.db import models
class Profile_url(models.Model):
    name = models.CharField(max_length=255)
    profile_url = models.URLField(max_length=500, unique=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name