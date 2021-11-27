from django import forms
from django.forms import fields
from user.models import User
class UserModel2Form(forms.ModelForm): 
    class Meta: 
        model = User
        fields = '__all__'