from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
)

urlpatterns = [
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
]
