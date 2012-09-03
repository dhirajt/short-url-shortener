from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'short.views.home', name='home'),
    # url(r'^short/', include('short.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^(\d+[A-Za-z]+)/','short.views.redirect'),
     url(r'^([A-Za-z]+\d+[A-Za-z]+)/','short.views.redirect'),
     url(r'^([A-Za-z]+\d+)/','short.views.redirect'),
     url(r'^(\d+[A-Za-z]+\d+)/','short.views.redirect')
     
)
