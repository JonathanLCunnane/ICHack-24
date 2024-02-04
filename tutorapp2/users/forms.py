from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Student, Tutor, Question, SubjectLevel, Review
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    credits = forms.IntegerField(widget=forms.NumberInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'credits')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        student = Student.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), credits=self.cleaned_data.get('credits'))
        return user
    

class TutorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    subjects_levels = forms.ModelMultipleChoiceField(
        queryset=SubjectLevel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'subjects_levels')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
        tutor = Tutor.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'), subject=self.cleaned_data.get('subjects_levels'))
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

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