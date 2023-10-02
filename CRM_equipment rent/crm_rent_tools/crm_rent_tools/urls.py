
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from core.views import index, about
from userprofile.forms import LoginForm

from userprofile.views import signup, myaccount
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/myaccount/', myaccount, name='myaccount'),
    path('dashboard/teams/', include('team.urls')),
    path('about/', about, name='about'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/detail/', include('team.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
