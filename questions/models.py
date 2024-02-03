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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.TextField()
    title = models.CharField(max_length=100)
    subjectLevel = models.ForeignKey('SubjectLevel', on_delete=models.CASCADE)
    # document = models.FileField(upload_to='uploads/') #TODO: FILE UPLOADS
    date = models.DateTimeField(auto_now_add=True)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subjects = models.ManyToManyField('SubjectLevel')

class SubjectLevel(models.Model):
    LEVEL_CHOICES = [
        ('A', 'A level'),
        ('G', 'GCSE'),
        ('K', 'KS3'),
    ]
    SUBJECT_CHOICES = [
        ('CS', 'Computer Science'),
        ('M', 'Maths'),
        ('P', 'Physics'),
        ('C', 'Chemistry'),
        ('B', 'Biology'),
    ]
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES)
    subject = models.CharField(max_length=5, choices=SUBJECT_CHOICES)
    def __str__(self):
        return f'{self.get_subject_display()} - {self.get_level_display()}'

class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
