from django.shortcuts import render
from django.views.generic.base import View

from user.models import User
from user.forms import UserToModel2Form

class UserListView(View):
    def get(self, request, *args, **kwargs): 
        users = User.objects.all()
        context = {'users': users, }
        return render(request, 'user/listUsers.html', context)


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'form' : UserToModel2Form}
        return render(request, "user/createUser.html", context) 

    def post(self, request, *args, **kwargs):
        pass 
