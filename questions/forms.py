from django import forms
from .models import User, Question, SubjectLevel, Tutor, Student, Review
from django import forms
from django.contrib.auth import get_user_model

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'email', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

class TutorSignUpForm(forms.ModelForm):
    subjects_levels = forms.ModelMultipleChoiceField(
        queryset=SubjectLevel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'email', )


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
            self.save_m2m()  # Save form's many-to-many field data
        return user

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