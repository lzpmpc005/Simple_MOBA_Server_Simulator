from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example, name='example'),
    path('create_player/', views.create_player, name='create_player'),
    path('create_character/', views.create_character, name='create_character'),

]