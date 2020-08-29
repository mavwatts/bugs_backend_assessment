from django.contrib import admin
from bugtracker_app.models import MyUser, Ticket

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Ticket)