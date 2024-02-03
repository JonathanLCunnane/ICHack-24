from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, TutorSignUpForm

def index(request):
    return render(request, 'layout.html')

def register(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            form = StudentSignUpForm(request.POST)
        else:
            form = TutorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'register.html', {'form': form})

def questionForm(request):
    return render(request, 'questionForm.html',{'user':{
        'username':'testuser',
    }})