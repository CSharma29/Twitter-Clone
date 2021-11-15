from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from User_Profile.models import Profile
import random
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null = True)
    tags = TaggableManager()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def get_title(self):
        return str(self.content)[:30] + str(random.randint(0, 10000))
    
    def __str__(self):
        return str(self.content)[:100]
    
    class Meta:
        ordering = ('-created',)
