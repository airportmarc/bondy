from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^new/$',
        view=views.CreateTrip.as_view(),
        name='add'
    ),
    url(
        regex=r'^(?P<pk>[\d]+)/$',
        view=views.ViewTrip.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UpdateTrip.as_view(),
        name='update'
    ),
    url(
        regex=r'^$',
        view=views.ViewAll.as_view(),
        name='view'
    ),
    url(
        regex=r'^delete/(?P<pk>[\d]+)/$',
        view=views.DeleteTrip.as_view(),
        name='delete'
    ),
]
