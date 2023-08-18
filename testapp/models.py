from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import requests
import datetime

# Create your models here.
class UserProfile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, default='')
    date = models.DateField(default=datetime.date.today)
    followers = models.IntegerField(default=0)
    time = models.TimeField(default='11:11')

class Repository(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=150, default='')
    stars = models.IntegerField(default=0)

def user_name(n):
    var1 = "https://api.github.com/users/"
    var2 = n
    str = "".join([var1, var2])
    response_user = requests.get(str)
    js = response_user.json()
    return js

def repos(m):
    var1 = "https://api.github.com/users/"
    var2 = m
    var3 = "".join([var1, var2])
    var4 = "/repos"
    str = "".join([var3, var4])
    response_repo = requests.get(str)
    js_repo = response_repo.json()
    return js_repo

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        jso = user_name(instance.username)
        profile.name = instance.first_name
        profile.followers = jso['followers']
        js_temp = jso['updated_at']
        profile.date = js_temp[0:10]
        profile.time = js_temp[11:19]
        profile.save()
        repo = repos(instance.username)
        js_number = len(repo)
        list_repo = []
        for i in range(0, js_number):
            temp = Repository.objects.create(owner=profile, repo_name=repo[i]['name'], stars=repo[i]['stargazers_count'])
            list_repo.append(temp)






    