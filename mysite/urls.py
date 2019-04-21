from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
]
