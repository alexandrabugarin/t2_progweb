import sys
sys.path.append("..")
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from catalog.serializer import *
from catalog.models import *
from user.serializer import*
from user.models import *

def home(request):
    return render(request, 'register/home.html')

def publicacao(request):
    publicacoes = PublicacaoSerializer(Publicacoes.objects.all(), many=True).data
    return render(request, 'register/publicacao.html', {'publicacoes': publicacoes})

def registerUser(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sec-login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register/cadastro.html', context)

def profile(request):
    usuarios = UserSerializer(request.user).data
    return render(request, 'register/profile.html', {'User': usuarios})

def userForm(request):
    return render(request, 'register/user_form.html')