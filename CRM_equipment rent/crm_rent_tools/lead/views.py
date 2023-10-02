
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddLeadForm, AddCommentForm, AddFileForm
from .models import Lead, Comment

from client.models import Client, Comment as ClientComment
from team.models import Team

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

    return render(request, 'lead/leads_list.html',{'leads':leads})

@login_required
def lead_add_file(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.team = request.user.userprofile.active_team
            file.lead_id = pk
            file.created_by = request.user
            file.save()

            return redirect('leads_detail', pk=pk)
    return redirect('leads_detail', pk=pk)


@login_required
def leads_detail(request,pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':  # добавляем комментарии
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = request.user.userprofile.active_team
            comment.created_by = request.user
            comment.lead = lead
            comment.save()

            return redirect('leads_detail', pk=pk)
    else:
        form = AddCommentForm()

    return render(request, 'lead/leads_detail.html', {
        'lead': lead,
        'form': form,
        'fileform': AddFileForm()
    })


@login_required
def leads_delete(request,pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'Лид успешно удален')

    return redirect('leads_list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method =='POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения успешно сохранены')
            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
    return render(request, 'lead/leads_edit.html', {'lead': lead,'form':form})




@login_required
def add_lead(request):
    team =request.user.userprofile.active_team
    if request.method =='POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():

            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = request.user.userprofile.active_team
            lead.save()

            messages.success(request, 'Лид успешно создан')

            return redirect('leads_list')
    else:
        form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form': form,
                                                  'team':team})


@login_required
def convert_to_client(request,pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = request.user.userprofile.active_team

    client = Client.objects.create(
        name=lead.name,
        tel_number=lead.tel_number,
        description=lead.description,
        created_by=request.user,
        team =team,

    )
    lead.converted_to_client = True
    lead.save()

    comments = lead.comments.all() #Соханение комментариев Лида при переходе в раздел Клиентов

    for comment in comments:
        newcomment = ClientComment.objects.create(
            client=client,
            content=comment.content,
            created_by=comment.created_by,
            team=team
        )
    messages.success(request, 'Лид переведен в клиенты.')

    return redirect('leads_list')


