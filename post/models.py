from django.db import models
# from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField()
    text =models.TextField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        
        
        
class Vote(models.Model):
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    
