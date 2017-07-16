from django.conf.urls import url

from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_title>[a-zA-Z0-9 _-]+)/$', views.detail, name='detail'),
]
