from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    firstName = models.CharField(max_length=200, blank=True)
    lastName = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default="no bio ...",max_length=400)
    email = models.EmailField(max_length=200,blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default="avatar.png",upload_to='avatar/')
    friends=models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

