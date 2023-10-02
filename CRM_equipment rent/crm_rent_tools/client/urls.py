from django.urls import path
from .import views


urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('<int:pk>/', views.clients_detail, name='clients_detail'),
    path('add_client/', views.add_client, name='add_client'),
    path('<int:pk>/add_comment/', views.clients_detail, name='add_comment_client'),
    path('<int:pk>/delete/', views.clients_delete, name='clients_delete'),
    path('<int:pk>/add-file/', views.client_add_file, name='add_file'),
    path('<int:pk>/edit/', views.clients_edit, name='clients_edit'),
    path('export/', views.clients_export, name='export'),

]