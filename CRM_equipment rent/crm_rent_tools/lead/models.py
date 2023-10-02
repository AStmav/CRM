from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from team.models import Team


class Lead(models.Model):

    COLD ='Холодный'
    WARM ='Телпый'
    HOT = 'Горячий'
    #классификация лидов (степень прогрева)


    CHOICES_PRIORITY = (
        (COLD,'Холодный'),
        (WARM,'Телпый'),
        (HOT, 'Горячий'),
    )

    NEW = 'Новый лид'
    CONTACTED = 'Взят в работу'
    WON = 'Успех'
    LOST = 'Временно потерян'
    CALLBACK = 'Перезвонить'

    CHOICES_STATUS = (
        (NEW, 'Новый'),
        (CONTACTED, 'Взят в работу'),
        (WON, 'Успех'),
        (LOST, 'Временно потерян'),
        (CALLBACK, 'Перезвонить'),
        )

    team =models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tel_number = PhoneNumberField(unique=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True)

    priority = models.CharField(max_length=20, choices=CHOICES_PRIORITY, default=WARM)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=NEW)
    converted_to_client = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name, self.tel_number, self.status, self.priority

class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='lead_comments', on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='lead_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username


class LeadFile(models.Model):
    team = models.ForeignKey(Team, related_name='lead_files', on_delete=models.CASCADE)
    client = models.ForeignKey(Lead, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='leadtfiles')
    created_by = models.ForeignKey(User, related_name='lead_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username



# Create your models here.
