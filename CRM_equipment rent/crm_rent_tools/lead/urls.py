from django.urls import path
from .import views

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
    path('<int:pk>/add_comment/', views.leads_detail, name='add_comment_lead'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', views.leads_edit, name='leads_edit'),
    path('<int:pk>/convert/', views.convert_to_client, name='convert_to_client'),
    path('add_lead/', views.add_lead, name='add_lead'),
    path('<int:pk>/add_file/', views.lead_add_file, name='add_file_lead'),


]