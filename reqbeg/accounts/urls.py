from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns = [ 
url(r'^signup/$', views.signuppage , name = 'signuppage'),
url(r'^login/$',views.loginpage, name = 'loginpage'),
url(r'^logout/$',views.logoutpage, name = 'logoutpage'),

]