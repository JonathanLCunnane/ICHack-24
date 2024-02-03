from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Question, SubjectLevel, Tutor, Student, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )


class StudentSignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        pass
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user

class TutorSignUpForm(CustomUserCreationForm):
    subjects_levels = forms.ModelMultipleChoiceField(
        queryset=SubjectLevel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(CustomUserCreationForm.Meta):
        pass

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