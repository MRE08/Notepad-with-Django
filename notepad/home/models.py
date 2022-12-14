from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now=True, null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    
    def __str__(self):
        return self.title
    