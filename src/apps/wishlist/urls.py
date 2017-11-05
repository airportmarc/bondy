from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^new/$',
        view=views.CreateWish.as_view(),
        name='add'
    ),
    url(
        regex=r'^(?P<pk>[\d]+)/$',
        view=views.ViewWish.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UpdateWish.as_view(),
        name='update'
    ),
    url(
        regex=r'^$',
        view=views.ListWish.as_view(),
        name='list'
    ),
    url(
        regex=r'^delete/(?P<pk>[\d]+)/$',
        view=views.DeleteWish.as_view(),
        name='delete'
    ),
]
