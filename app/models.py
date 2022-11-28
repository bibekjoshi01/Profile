from django.db import models
from django.contrib.auth.models import User
# Create your models here.

relations = (
    ('Single','Single'),
    ('In a Relationship', 'In a Relationship'),
    ('Married','Married'),
)

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=150)
    relationship = models.CharField(choices=relations, max_length=20, default='Single')
    bio = models.CharField(max_length=150, null=True)
    about = models.TextField(blank=True)
    education = models.CharField(max_length=75, blank=True)
    email = models.CharField(max_length=50)
    birth_date = models.DateField()
    profession = models.CharField(max_length=50, blank=True)
    facebook_url = models.URLField(max_length=500, blank=True)
    twitter_url = models.URLField(max_length=500, blank=True)
    stack_url = models.URLField(max_length=500, blank=True)
    github_url = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return self.full_name
