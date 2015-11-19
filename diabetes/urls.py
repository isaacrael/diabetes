from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'diabetes_manager.views.index', name='index'),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
