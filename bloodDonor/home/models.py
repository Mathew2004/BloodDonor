from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default="Not Given")
    phn1 = models.CharField(max_length=30)
    phn2 = models.CharField(max_length=30, default="Not Given")
    fblink = models.CharField(max_length=300, default="Not Given")
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    bg = models.CharField(max_length=30)
    img = models.ImageField(upload_to="", default="media/user.jpeg")

    def __str__(self):
        return self.fname+' '+self.lname

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phn = models.CharField(max_length=50)
    msg = models.TextField()

    def __str__(self):
        return self.name
        
class DonorStory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phn = models.CharField(max_length=50)
    msg = models.TextField()
    imgname = models.CharField(max_length=200)
    fblink = models.CharField(max_length=400, default="")

    def __str__(self):
        return "Story by "+ self.name
