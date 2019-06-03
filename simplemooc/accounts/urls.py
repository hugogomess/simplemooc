from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('cadastro/', views.register, name='register'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),

]