"""Schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from SchoolApp.views import SchoolApp, students, teachers


urlpatterns = [
    url('', include('SchoolApp.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/signup/', SchoolApp.SignUpView.as_view(), name='signup'),
    url('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    url('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]