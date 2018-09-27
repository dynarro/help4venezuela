from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from help4vzl.forms import LoginForm


urlpatterns = [
    url(r'^$', views.postulation, name='postulation'),
    url(r'^postulation/(?P<pk>\d+)/detail/$', views.postulation_detail, name='postulation_detail'),
    url(r'^postulation/(?P<pk>\d+)/edit/$', views.postulation_edit, name='postulation_edit'),
    url(r'^postulation/new/$', views.postulation_new, name='postulation_new'),
    url(r'^postulation/created/$', views.thankyoupage, name='thankyoupage'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
