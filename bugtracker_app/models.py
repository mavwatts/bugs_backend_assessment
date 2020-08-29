from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class MyUser(AbstractUser):
    pass

class Ticket(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=240)
    time_dates = models.DateTimeField(default=timezone.now)
    ticket_maker = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ticket_maker')
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='assigned_to', blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="completed_by", blank=True, null=True)
    New = 'N'
    In_progress = 'IP'
    Done = 'D'
    Invalid = 'Inv'
    STATUS_OF_TICKET = [
        (New, 'New'),
        (In_progress, 'In_progress'),
        (Done, 'Done'),
        (Invalid, 'Invalid'),
    ]
    ticket_status = models.CharField(choices= STATUS_OF_TICKET, max_length=3, default='N')

    def __str__(self):
        return self.title