from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
    AppointmentListView,
)

urlpatterns = [
    # List view
    re_path(r'^$', AppointmentListView.as_view(),
            name='list_appointments'),
    # Create view
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
]
