from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentDeleteView,
)

urlpatterns = [
    # List view
    re_path(r'^$', AppointmentListView.as_view(),
            name='list_appointments'),
    # Create view
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),

    # Delete view
    re_path(r'^(?P<pk>[0-9]+)/delete$',
            AppointmentDeleteView.as_view(),
            name='delete_appointment'),
]
