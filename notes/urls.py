from django.conf.urls import include, url
from django.contrib import admin
from . import views

appname = 'notes'
urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='index'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.create_note),
    url(r'^note/(?P<note_id>[0-9]+)/update/$', views.update_note, name='update'),
    url(r'^admin/', admin.site.urls),
]