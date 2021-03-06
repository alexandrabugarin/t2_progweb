"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.urls.conf import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User


urlpatterns = [
    #PAGINA 1: LOGIN 
    path('', LoginView.as_view(template_name="register/login.html"), name = 'sec-login'),
    #PAGINA 2: CADASTRO DE USUÁRIO
    path('accounts/register/', views.registerUser, name='cadastro'),
    path('accounts/finishRegister/<int:pk>/', UpdateView.as_view(
        template_name='register/user_form.html', 
        success_url=reverse_lazy('sec-profile'), 
        model= User, 
        fields=[
            'first_name', 
            'last_name', 
            'email',
        ],
        ),
        name='sec-userComplet'),
    #HOME
    path('publicacao', views.publicacao, name ='publicacao'),
    #PERFIL USUÁRIO
    path('accounts/profile/', views.profile, name='sec-profile'),
    #LOGIN ADMIN
    path('admin/', admin.site.urls, name='admin'),
    #LOGOUT
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-login'), ), name='sec-logout'),

]
