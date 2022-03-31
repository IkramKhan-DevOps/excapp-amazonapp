from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from pw_amazon_ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.website.urls', namespace='website')),
    path('accounts/', include('Apps.accounts.urls', namespace='accounts'))
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]