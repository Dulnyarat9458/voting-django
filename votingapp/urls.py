from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete'),
    path('home/',login_required( views.Home.as_view()), name='home'),
    path('home/confirmvote/',login_required(views.ConfirmVote.as_view()), name='confirmvote'),

]
