from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Model
    template_name = ".html"


# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# # Create your views here.
