import sys
sys.path.append("..")
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from user.models import *

admin.site.site_header = "Admin"

class PublicacoesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'texto')
    search_fields = ('titulo', 'texto')

admin.site.register(Publicacoes,PublicacoesAdmin)
admin.site.unregister(Group)
admin.site.register(User)