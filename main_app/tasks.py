from __future__ import absolute_import

import arrow
import dramatiq

from django.conf import settings
from twilio.rest import Client

from .models import Appointment
clinet = Client(settings.ACda05149c0b4d416716ba2ba9e217ae3b, settings.3d46e40bd95ee85114d46c387c78bc3c)


@dramatiq.actor
def send_sms_reminder(appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = 'Hi {0}. You have an appointment coming up at {1}.'.format(
        appointment.name, appointment_time.format('h:mm a'))

    client.messages.create(
        body=body,
        to=appointment.phone_number,
        from_=settings.8172668041,
    )
