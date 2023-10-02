from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from team.models import Team


def signup(request):

    if request.method=='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user =form.save()
            team = Team.objects.create(name='Название группы', created_by=user) # при создании нвго пользоваеля будет создаваться группа в которую он будет добавлять своих клиентов
            team.members.add(user)
            team.save()

            Userprofile.objects.create(user=user, active_team=team)

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {'form': form})



@login_required
def myaccount (request):
    team = request.user.userprofile.active_team

    return render(request, 'userprofile/myaccount.html',{'team':team})
