from django.db import models


# Create your models here.
class userInfo(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    ssn = models.IntegerField(primary_key=True,max_length=11)
    designation = models.IntegerField()
    pw = models.CharField(max_length=200)

class userProfile(models.Model):
    ssn = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    doj = models.CharField(max_length=200)
    job = models.CharField(max_length=200)