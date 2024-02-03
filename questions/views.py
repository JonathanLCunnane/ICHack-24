from django.shortcuts import render
from .forms import StudentSignUpForm, TeacherSignUpForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        if 'student' in request.POST:
            form = StudentSignUpForm(request.POST)
        else:
            form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'register.html', {'form': form})