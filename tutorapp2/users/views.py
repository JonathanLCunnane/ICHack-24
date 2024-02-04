from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User, Question, SubjectLevel, Review
from .forms import StudentSignUpForm, TutorSignUpForm, LoginForm, QuestionForm, ReviewForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import student_required, tutor_required
from django.http import HttpResponse


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student-dashboard')
    

class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'users/tutor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tutor-dashboard')
    

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_student:
                return reverse('student-dashboard')
            elif user.is_tutor:
                return reverse('tutor-dashboard')
        else:
            return reverse('login')
        

@login_required
@student_required
def student_dashboard(request):
    form = QuestionForm()
    return render(request, 'users/student_dashboard.html', {'user': request.user, 'form': form})

@login_required
@tutor_required
def tutor_dashboard(request):
    return render(request, 'users/tutor_dashboard.html', {'user': request.user})

@login_required
@student_required
def get_help(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            #TODO: Save the question and tutor get
            return render(request, 'users/student_dashboard.html', {'form': form, 'valid': True, 'message': "Your question was submitted!"})
        return render(request, 'users/student_dashboard.html', {'form': form, 'valid': False, 'message': "Invalid Form! :("})
    else:
        form = QuestionForm()
    return render(request, 'users/student_dashboard.html', {'form': form})