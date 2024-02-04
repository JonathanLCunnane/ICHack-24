from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Student, Question, Tutor, Review, SubjectLevel

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

class TutorInline(admin.StackedInline):
    model = Tutor
    can_delete = False
    verbose_name_plural = 'tutor'


class StudentAdmin(BaseUserAdmin):
    inlines = [StudentInline]

class TutorAdmin(BaseUserAdmin):
    inlines = [TutorInline]


# admin.site.unregister(User)
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)

# admin.site.register(Student)
admin.site.register(Question)
# admin.site.register(Tutor)
admin.site.register(Review)
admin.site.register(SubjectLevel)

