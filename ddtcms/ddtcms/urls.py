from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ddtcms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
try:
    from local_urls import *
    #print 'local urls loaded'
except ImportError as e:
    print  e
    print 'local urls NOT loaded'
