from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team
from .forms import TeamForm


@login_required
def teams_list(request):
    teams = Team.objects.filter(members__in=[request.user])

    return render(request, 'team/teams_list.html', {'teams': teams})

@login_required
def teams_activate(request, pk):
    team = Team.objects.filter(members__in=[request.user]).get(pk=pk)
    userprofile = request.user.userprofile
    userprofile.active_team = team
    userprofile.save()

    return redirect('detail', pk=pk)


@login_required
def detail(request, pk):
    team = get_object_or_404(Team, members__in=[request.user], pk=pk)

    return render(request, 'team/detail.html', {'team': team})

@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)

    if request.method == "POST":
        form = TeamForm (request.POST, instance=team)

        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect('myaccount')
    else:

        form = TeamForm(instance=team)
    return render(request, 'team/edit_team.html', {'team':team, 'form':form})
# Create your views here.
