from django.conf.urls import url
from . import views


urlpatterns = [

url(r'^time/$',views.rockets,name='time'),
url(r'^spaceports/$',views.spaceports)



]
