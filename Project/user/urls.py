from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('list/', views.UserListView.as_view(), name='list-user'), 
    path('', views.UserListView.as_view(), name='home-user'), 
    path('create/', views.UserCreateView.as_view(), name='create-user'),
    ]