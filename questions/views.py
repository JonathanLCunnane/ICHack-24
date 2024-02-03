from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TutorSignUpForm, QuestionForm
from django.http import HttpResponseForbidden, HttpResponse


def index(request):
    return render(request, 'index.html')

def register_tutor(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TutorSignUpForm()
    return render(request, 'register.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TutorSignUpForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_student:
                    return redirect('student_dashboard')
                else:
                    return redirect('tutor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def student_dashboard(request):
    #TODO - BOTH VIEW AND HTML
    return render(request, 'student_dashboard.html')

@login_required
def tutor_dashboard(request):
    #TODO - BOTH VIEW AND HTML
    return render(request, 'tutor_dashboard.html')

def tutor_profile(request, tutor_id):
    
    return render(request, 'tutor_profile.html', {'tutor_id': tutor_id})

def student_profile(request, student_id):

    return render(request, 'student_profile.html')


@login_required
def get_help(request):
    # Students send questions
    if not request.user.is_student:
        return HttpResponseForbidden("You must be a student to access this page.")

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            #TODO - match with tutors
            return HttpResponse("Question sent")
    else:
        form = QuestionForm()
        return render(request, 'get_help.html', {'form': form})