from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^good/$', views.addlike),
    url(r'^bad/$', views.adddislike),
]