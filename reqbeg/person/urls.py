from django.urls import path
from django.conf.urls import url
from . import views
app_name ='persons'
urlpatterns = [
    url(r'^$', views.leaders, name = 'abf' ),
    url(r'^(?P<slug>[\w]+)/$', views.abc, name = 'hello'),

]