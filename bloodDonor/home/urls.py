from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('users/', views.users, name='Users'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='SignUp'),
    path('signupStatus/', views.handleSignup, name='SignhandleSignupUp'),
    path('login/', views.loginpage, name='loginform'),
    path('loginStatus/', views.handeLogin, name='loginStatus'),
    path('logout/', views.handelLogout, name='handelLogout'),
    path('users/<str:user>', views.userProfile, name='userProfile'),
    path('search/', views.search, name='search'),
    path('story/<str:user>', views.donorStory, name='donorStory'),
    path('editprofile/', views.editProfile, name='editprofile'),
    path('uploadPic/', views.uploadPic, name='uploadPic'),
    path('dltprofile/', views.DltProfile, name='DltProfile'),

]

