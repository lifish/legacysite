from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legacysite.views.home', name='home'),
    # url(r'^legacysite/', include('legacysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	# for test 
	url(r'^$', 'article.views.temp'),
	(r'^ckeditor/', include('ckeditor.urls')),
)
