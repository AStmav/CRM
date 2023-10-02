from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/edit/', views.edit_team, name='edit_team'),
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.teams_list, name='list'),
    path('<int:pk>/activate/', views.teams_activate, name='activate'),

]