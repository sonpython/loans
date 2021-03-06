from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loans.views.home', name='home'),
    # url(r'^loans/', include('loans.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^django/admin/', include(admin.site.urls)),

    url(r'', include('web.urls')),  
    url('', include('social.apps.django_app.urls', namespace='social')),


    # Uncomment the next line to enable the admin:
    url(r'^backoffice/', include('backoffice.urls')),
    url(r'^backoffice/', include('graph.urls')),
)
