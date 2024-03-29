from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    # Deal with registering
    path("register-tutor/", views.register_tutor, name="register_tutor"),
    path("register-student/", views.register_student, name="register_student"),
    # Dashboards
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("tutor-dashboard/", views.tutor_dashboard, name="tutor_dashboard"),
    # Profiles
    path("student/{student_id}/", views.student_profile, name="student_profile"),
    path("tutor/<int:tutor_id>/", views.tutor_profile, name="tutor_profile"),
    # Get help
    path("get-help/", views.get_help, name="get_help"),
]

# Deal with registration - both tutor and student redirect to respective dashboard - dylan
# Deal with login - redirect to respective dashboard - richard
# Deal with displaying tutor and student profiles - jonni (doing tutor profiles)
# Deal with displaying tutors available for help
