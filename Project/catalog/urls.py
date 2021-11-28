from django.urls import path
from user import views

app_name = 'publicacoes'

urlpatterns = [
    path('list/', views.publicacaoListView.as_view(), name='list-publicacao'), 
    path('', views.publicaoListView.as_view(), name='home-publicacao'), 
    path('create/', views.PublicacaoCreateView.as_view(), name='create-publicacao'),
    path('update/<int:pk>/', views.publicacaoUpdateView.as_view(),name='update-publicacao'),
    path('delete/<int:pk>/', views.publicacaoDeleteView.as_view(),name='delete-publicacao'),
    ]