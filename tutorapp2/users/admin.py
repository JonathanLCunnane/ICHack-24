from django.contrib import admin
from .models import User, Question, Student, Tutor, SubjectLevel, Review

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(SubjectLevel)
admin.site.register(Review)