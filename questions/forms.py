from django import forms
from .models import Question, SubjectLevel, Tutor, Student, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

# class StudentSignUpForm(UserCreationForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

class StudentSignUpForm(UserCreationForm):
    credits = forms.IntegerField()

    class Meta:
        model = User
        fields = ('credits',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user, credits=self.cleaned_data['credits'])
        return student

class TutorSignUpForm(UserCreationForm):
    subjects_levels = forms.ModelMultipleChoiceField(
        queryset=SubjectLevel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = User
        fields = ('subjects_levels',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tutor = True
        user.save()
        tutor = Tutor.objects.create(user=user, subjects_levels=self.cleaned_data['subjects_levels'])
        return tutor
    
# class TutorSignUpForm(forms.ModelForm):

#     class Meta:
#         model = Tutor
#         fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question', 'subjectLevel']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']

class SubjectLevelForm(forms.ModelForm):
    class Meta:
        model = SubjectLevel
        fields = ['subject', 'level']