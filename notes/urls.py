from django.conf.urls import include, url
from . import views

appname = 'notes'
urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='index'),
    url(r'^note/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.create_note),
    url(r'^note/(?P<slug>[-\w]+)/update/$', views.update_note, name="update"),
]