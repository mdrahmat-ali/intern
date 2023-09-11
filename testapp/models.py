from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

class Artist(models.Model):
    name=models.CharField(max_length=30)
    work=models.CharField(max_length=100)

class Work(models.Model):
    name=models.CharField(max_length=64)
    work_type=models.CharField(max_length=100)

    

