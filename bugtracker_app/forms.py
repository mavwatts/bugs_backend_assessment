from django import forms
from bugtracker_app.models import MyUser, Ticket

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

