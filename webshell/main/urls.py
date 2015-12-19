from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^model$', views.model, name='index'),
    url(r'^newmodel$', views.newmodel, name='index'),
]
