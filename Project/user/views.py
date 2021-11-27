from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from user.models import User
from user.forms import UserModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class UserListView(View):
    def get(self, request, *args, **kwargs): 
        users = User.objects.all()
        context = {'users': users, }
        return render(request, 'user/listUsers.html', context)

class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'form' : UserModel2Form}
        return render(request, "user/createUser.html", context) 

    def post(self, request, *args, **kwargs):
        form = UserModel2Form(request.POST)
        if form.is_valid(): 
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse_lazy('user:list-user'))
        pass 

class UserUpdateView(View): 
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk = pk)
        form = UserModel2Form(instance=user)
        context = {'form' : form}
        return render(request, 'user/updateUser.html', context)

    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk = pk)
        form = UserModel2Form(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse_lazy('user:list-user'))
        else:
            context = {'form' : form,} 
            return render(request, 'user/updateUser.html', context)

class UserDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk = pk)
        context = {'user' : user}
        return render(request, 'user/deleteUser.html', context)
        pass

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk = pk)
        user.delete()
        return HttpResponseRedirect(reverse_lazy('user:list-user'))