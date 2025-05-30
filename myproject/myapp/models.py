from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)  # Use the same ID as the mock API
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.title

