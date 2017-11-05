
from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^new/$', views.MakeInviteView.as_view(), name='new')
    ]




