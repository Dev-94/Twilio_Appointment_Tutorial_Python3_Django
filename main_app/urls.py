from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
    AppointmentListView
)

urlpatterns = [
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
    re_path(r'^$', AppointmentListView.as_view(),
            name='list_appointments'),
]
