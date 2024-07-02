from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class register(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    fullname=models.CharField(null=True, max_length=20)
    contact=models.IntegerField(null=True)
    email=models.CharField(null=True,max_length=30)
    address=models.CharField(null=True,max_length=30)
    def __str__(self):
        return self.fullname

class question(models.Model):
    qno=models.IntegerField(null=True)
    question=models.CharField(null=True,max_length=100)
    optiona=models.CharField(null=True,max_length=50)
    optionb=models.CharField(null=True,max_length=50)
    optionc=models.CharField(null=True,max_length=50)
    optiond=models.CharField(null=True,max_length=50)
    answer=models.CharField(null=True,max_length=50)
    def __str__(self):
        return self.question


