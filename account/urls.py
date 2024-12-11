
from django.urls import path
from . import views

urlpatterns = [
    path(route='auth/signup', view=views.signUpPage, name="SignUp"),
    path(route='auth/signin', view=views.loginUpPage, name='login'),
    path(route='home', view=views.getData, name='home')
]