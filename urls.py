from django.conf.urls import patterns, url

from . import views, APP_NAME

urlpatterns = patterns('',
                       # app urls
   url(r'^$', views.index, name='%s.index' % APP_NAME),

                       )
