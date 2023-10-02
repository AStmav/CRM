from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lead.models import Lead
from client.models import Client
from team.models import Team


@login_required         #декоратор проверки авторизации пользователя
def dashboard(request):
    team = request.user.userprofile.active_team # Получаем команду пользователя
    leads =Lead.objects.filter(team=team).order_by('-created_at')[0:5]#Получаем последние 5 лидов для этой команды, отсортированных по времени создания
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html',{'leads':leads,'clients':clients})



