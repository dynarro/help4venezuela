from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.postulation, name='postulation'),
    url(r'^postulation/(?P<pk>\d+)/detail/$', views.postulation_detail, name='postulation_detail'),
    url(r'^postulation/(?P<pk>\d+)/edit/$', views.postulation_edit, name='postulation_edit'),
    url(r'^postulation/new/$', views.postulation_new, name='postulation_new'),
]
