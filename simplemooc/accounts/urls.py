from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('cadastro/', views.register, name='register'),

]