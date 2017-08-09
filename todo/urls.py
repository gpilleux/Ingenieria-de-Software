from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),

    url(r'^todo/', views.add, name='add'),
    url(r'^add', views.add, name='add'),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete),
    url(r'^subir/(?P<id>\w{0,50})/$', views.subir),
    url(r'^bajar/(?P<id>\w{0,50})/$', views.bajar)
]
