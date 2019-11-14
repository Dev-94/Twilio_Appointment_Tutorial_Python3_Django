from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = "Appointment successfully created."


# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# # Create your views here.
