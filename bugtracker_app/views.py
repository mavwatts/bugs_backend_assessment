from django.shortcuts import render, HttpResponseRedirect, reverse
from bugtracker_app.models import MyUser, Ticket
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bugtracker_app.forms import LoginForm, AddTicketForm


# Create your views here.
@login_required
def index_view(request):
    my_ticket = Ticket.objects.all()
    return render(request, 'index.html', {'my_ticket': my_ticket})
 
@login_required
def add_ticket(request):
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                ticket_maker = request.user,
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password')) 
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def ticket_detail_view(request):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail', {"tickets": my_ticket})

def user_detail_view(request):
    return render(request, user_detail_view)

@login_required
def edit_ticket_view(request, ticket_id):
    ticket_instance = Ticket.objects.filter(id=ticket_id).first()
    form = AddTicketForm(instance=ticket_instance)
    if request.method == "POST":
            form = AddTicketForm(request.POST, instance=ticket_instance)
            form.save()
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'generic_form.html', {'form': form})
