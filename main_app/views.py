from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView


from .models import Appointment


class AppointmentListView(ListView):
    model = Appointment


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = "Appointment successfully created."


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully updated.'


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('list_appointments')
