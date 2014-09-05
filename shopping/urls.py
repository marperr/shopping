import os
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopping.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(os.path.dirname(__file__), 'static/media' )}),
	(r'^static(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(os.path.dirname(__file__), 'static' )}),

	url(r'^$', 'products.views.home'), 	
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^products/$', 'products.views.products'),	
   	url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
	url(r'^contact/$', 'contact.views.contact'),
	
	
	
)


