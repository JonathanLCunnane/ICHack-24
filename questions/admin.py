from django.contrib import admin
from .models import User, Student, Question, Tutor, Review

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Tutor)
admin.site.register(Review)