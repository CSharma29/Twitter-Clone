from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from User_Profile.models import Info_Profile
# Create your models here.

class Tweet(models.Model):
    author = models.ForeignKey(Info_Profile, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null = True)
    tags = TaggableManager()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.content[:100]
    
    class Meta:
        ordering = ('-created',)
