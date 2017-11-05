from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^new/$',
        view=views.CreateProperty.as_view(),
        name='add'
    ),
    url(
        regex=r'^(?P<pk>[\d]+)/$',
        view=views.ViewProperty.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UpdateProperty.as_view(),
        name='update'
    ),
    url(
        regex=r'^$',
        view=views.ListProperty.as_view(),
        name='list'
    ),
    url(
        regex=r'^delete/(?P<pk>[\d]+)/$',
        view=views.DeleteProperty.as_view(),
        name='delete'
    ),
]
