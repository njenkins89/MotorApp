from django.conf.urls import url

from . import views

app_name = 'MotorsConfig'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^single/$', views.singleMotor, name = 'single')
]
