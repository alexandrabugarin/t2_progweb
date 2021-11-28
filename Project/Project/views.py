from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'register/home.html')

def publicacao(request):
    return render(request, 'register/publicacao.html')

def registerUser(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sec-home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register/register.html', context)

def profile(request):
      return render(request, 'register/profile.html')