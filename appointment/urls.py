from django.conf.urls import include
from django.conf.urls import re_path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # paths to home and main_app.urls
    re_path(r'^$', TemplateView.as_view(
        template_name='index.html'), name='home'),
    re_path(r'^appointments/', include('main_app.urls')),    # Django admin
    re_path(r'^admin/', admin.site.urls),
]
