from django.db import models
# Create your models here.

class Info_Profile(models.Model):
    user_name = models.CharField(max_length=500, unique = True)
    bio = models.TextField(default='no bio...')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profiles_posts(self):
        pass
    def __str__(self):
        return str(self.user_name)
    
    class Meta:
        ordering = ('-created',)