# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    credits = models.IntegerField(default=0)

class Question(models.Model):
    LEVEL_CHOICES = [
        ('A', 'A level'),
        ('G', 'GCSE'),
        ('K', 'KS3'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.TextField()
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default='A')
    # document = models.FileField(upload_to='uploads/') #TODO: FILE UPLOADS
    date = models.DateTimeField(auto_now_add=True)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
