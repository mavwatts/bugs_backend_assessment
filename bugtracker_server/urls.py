"""bugtracker_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bugtracker_app.views import index_view, login_view, logout_view, add_ticket, user_detail_view, edit_ticket_view, ticket_detail_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('addticket/', add_ticket),
    path('ticket/<int:ticket_id>/edit/', edit_ticket_view),
    path('ticket/<int:ticket_id>/', ticket_detail_view),
    path('user/<int:user_id>/', user_detail_view),
    path('admin/', admin.site.urls),
]
