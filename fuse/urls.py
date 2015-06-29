from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^submit/$', views.submit, name='submit'),
  url(r'^raspcheck/$', views.check, name='raspcheck'),
  url(r'^verif/$', views.verify, name='verify'),
]
