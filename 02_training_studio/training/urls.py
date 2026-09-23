from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("classes/", views.classes, name="classes"),
    path("classes/<int:id>/", views.classes_detail, name="classes_detail"),
    path("schedules/", views.schedules, name="schedules"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
]
