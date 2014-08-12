from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^login/$', 'blog.views.login_user'),
    (r'^$', 'blog.views.blog'),
    (r'^cpanel/$', 'blog.views.cpanel'),
    (r'^blog/$', 'blog.views.blog'),
    (r'^logout/$', 'blog.views.logout_view'),
    (r'^addnews/$', 'blog.views.add_news'),
    (r'^editnews/(\d+)/$', 'blog.views.edit_news'),
    (r'^deletenews/(\d+)/$', 'blog.views.delete_news'),
    url(r'^admin/', include(admin.site.urls)),
)
