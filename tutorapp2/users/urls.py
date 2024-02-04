from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.student_dashboard, name="student-dashboard"),
    path("tutor/", views.tutor_dashboard, name="tutor-dashboard"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/student/", views.StudentSignUpView.as_view(), name="student-signup"),
    path("signup/tutor/", views.TutorSignUpView.as_view(), name="tutor-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("get-help/", views.get_help, name="get-help"),
    #Profiles need to be implemented - TODO both student and tutors
]