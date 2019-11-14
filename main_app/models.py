from __future__ import unicode_literals

import redis

from django.core.exceptions import validationError
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow


@python_2_unicode_compatible
class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='UTC')


task_id = models.CharField(max_length=50, black=True, editable=False)
created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return 'Appointment #{0} - {1}'.format(self.pk, self.name)
