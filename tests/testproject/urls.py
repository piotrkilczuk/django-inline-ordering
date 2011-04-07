from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url' : '/admin/'}),
    
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^testapp/', include('testapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
